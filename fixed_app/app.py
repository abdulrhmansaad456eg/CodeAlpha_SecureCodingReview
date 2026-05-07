from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import sqlite3
import os
import secrets

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY')
if not app.secret_key:
    app.secret_key = secrets.token_hex(32)
    print("WARNING: Using auto-generated secret key. Set SECRET_KEY environment variable for production.")

app.debug = False

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=3600
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'users.db')

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}
MAX_FILE_SIZE = 5 * 1024 * 1024

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def get_db_connection():
    conn = sqlite3.connect(DATABASE, timeout=20)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            is_admin INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    sample_users = [
        ('admin', generate_password_hash('admin123', method='pbkdf2:sha256'), 'admin@company.com', 1),
        ('john_doe', generate_password_hash('password123', method='pbkdf2:sha256'), 'john@example.com', 0),
        ('jane_smith', generate_password_hash('welcome2024', method='pbkdf2:sha256'), 'jane@example.com', 0),
        ('test_user', generate_password_hash('test12345', method='pbkdf2:sha256'), 'test@example.com', 0)
    ]
    
    for user in sample_users:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO users (username, password, email, is_admin)
                VALUES (?, ?, ?, ?)
            ''', user)
        except sqlite3.IntegrityError:
            pass
    
    conn.commit()
    conn.close()
    print("Database initialized successfully with hashed passwords")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_input(data, max_length=100):
    if not data or not isinstance(data, str):
        return None
    sanitized = data.strip()[:max_length]
    return sanitized


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = validate_input(request.form.get('username', ''))
        password = request.form.get('password', '')
        
        if not username or not password:
            flash('Username and password are required', 'error')
            return render_template('login.html')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                'SELECT * FROM users WHERE username = ?',
                (username,)
            )
            user = cursor.fetchone()
            
            if user and check_password_hash(user['password'], password):
                session.clear()
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['is_admin'] = user['is_admin']
                session.permanent = True
                flash(f'Welcome back, {user["username"]}!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials', 'error')
        except sqlite3.Error:
            flash('An error occurred. Please try again.', 'error')
        finally:
            conn.close()
    
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, username, email FROM users')
    users = cursor.fetchall()
    
    conn.close()
    
    return render_template('dashboard.html', 
                         username=session.get('username'),
                         is_admin=session.get('is_admin'),
                         users=users)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'user_id' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('login'))
    
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('dashboard'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('dashboard'))
    
    if file and allowed_file(file.filename):
        original_filename = secure_filename(file.filename)
        
        import time
        filename = f"{int(time.time())}_{original_filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        file.save(filepath)
        
        file_size = os.path.getsize(filepath)
        if file_size > MAX_FILE_SIZE:
            os.remove(filepath)
            flash('File too large. Maximum size is 5MB.', 'error')
            return redirect(url_for('dashboard'))
        
        flash(f'File "{original_filename}" uploaded successfully', 'success')
    else:
        allowed = ', '.join(ALLOWED_EXTENSIONS)
        flash(f'Invalid file type. Allowed types: {allowed}', 'error')
    
    return redirect(url_for('dashboard'))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    safe_filename = secure_filename(filename)
    
    if not safe_filename:
        abort(404)
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
    
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        abort(404)
    
    real_filepath = os.path.realpath(filepath)
    real_upload_folder = os.path.realpath(app.config['UPLOAD_FOLDER'])
    
    if not real_filepath.startswith(real_upload_folder):
        abort(403)
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], safe_filename)


@app.route('/search')
def search():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    query = validate_input(request.args.get('q', ''), max_length=50)
    
    if not query:
        return render_template('dashboard.html', 
                             username=session.get('username'),
                             search_query='',
                             search_results=[],
                             users=[])
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    search_pattern = f'%{query}%'
    cursor.execute(
        'SELECT * FROM users WHERE username LIKE ?',
        (search_pattern,)
    )
    results = cursor.fetchall()
    conn.close()
    
    return render_template('dashboard.html', 
                         username=session.get('username'),
                         search_query=query,
                         search_results=results,
                         users=[])


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out securely', 'success')
    return redirect(url_for('login'))


@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response


@app.errorhandler(404)
def not_found(error):
    return render_template('login.html'), 404


@app.errorhandler(500)
def internal_error(error):
    flash('An internal error occurred. Please try again later.', 'error')
    return redirect(url_for('login'))


if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    
    print("Secure Flask Application Starting...")
    print("Remember to set SECRET_KEY environment variable for production")
    app.run(host='127.0.0.1', port=5000, debug=False)
