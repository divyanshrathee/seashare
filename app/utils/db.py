import sqlite3
import os
from app.utils.security import hash_password

DB_FILE = 'database.db'

def init_db():
    if not os.path.exists(DB_FILE):  # Only create if it doesn't exist
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        # Create users table
        c.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL UNIQUE,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Create quarters table
        c.execute('''
            CREATE TABLE quarters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL UNIQUE,
                rank TEXT NOT NULL,
                name TEXT NOT NULL,
                contact TEXT NOT NULL,
                building TEXT NOT NULL,
                notice_period TEXT NOT NULL
            )
        ''')

        # Insert dummy users
        users = [
            (1001, 'Vishal', hash_password('vishal123')),
            (1002, 'Kunal', hash_password('kunal123')),
            (1003, 'Ajay', hash_password('ajay123')),
            (1004, 'Rohit', hash_password('rohit123')),
            (1005, 'Keshav', hash_password('keshav123')),
        ]
        c.executemany('INSERT INTO users (user_id, username, password) VALUES (?, ?, ?)', users)

        conn.commit()
        conn.close()
