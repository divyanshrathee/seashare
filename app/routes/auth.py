from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3
from app.utils.security import hash_password

auth_bp = Blueprint('auth', __name__)

DB_FILE = 'database.db'

@auth_bp.route('/')
def home():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        hashed_password = hash_password(password)

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE user_id = ? AND password = ?', (user_id, hashed_password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[1]
            session['username'] = user[2]
            return redirect(url_for('post.post_quarter'))
        else:
            error = 'Invalid User ID or Password. Please try again.'

    return render_template('login.html', error=error)

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
