from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
import sqlite3
import os

app = Flask(__name__)

app.secret_key = 'super_secret_key_12345_do_not_change'

app.debug = True

DATABASE = 'users.db'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
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
            is_admin INTEGER DEFAULT 0
        )
    ''')
    
    sample_users = [
        ('admin', 'admin123', 'admin@company.com', 1),
        ('john_doe', 'password123', 'john@example.com', 0),
        ('jane_smith', 'welcome2024', 'jane@example.com', 0),
        ('test_user', 'test12345', 'test@example.com', 0)
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
    print("Database initialized successfully")


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['is_admin'] = user['is_admin']
                flash(f'Welcome back, {user["username"]}!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password', 'error')
        except sqlite3.Error as e:
            flash(f'Database error: {str(e)}', 'error')
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
    
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        flash(f'File "{filename}" uploaded successfully', 'success')
    
    return redirect(url_for('dashboard'))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/search')
def search():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    query = request.args.get('q', '')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    search_query = f"SELECT * FROM users WHERE username LIKE '%{query}%'"
    
    try:
        cursor.execute(search_query)
        results = cursor.fetchall()
    except sqlite3.Error:
        results = []
    finally:
        conn.close()
    
    return render_template('dashboard.html', 
                         username=session.get('username'),
                         search_query=query,
                         search_results=results,
                         users=[])


@app.route('/debug')
def debug_info():
    import sys
    info = {
        'secret_key': app.secret_key,
        'debug_mode': app.debug,
        'database': DATABASE,
        'upload_folder': UPLOAD_FOLDER,
        'python_version': sys.version,
        'environment': dict(os.environ)
    }
    return info


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    
    app.run(host='0.0.0.0', port=5000, debug=True)
