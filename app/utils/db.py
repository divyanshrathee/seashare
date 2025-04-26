# app/init_db.py

import sqlite3
import os
from app.database.schema import CREATE_USERS_TABLE, CREATE_QUARTERS_TABLE
from app.database.dummy_data import DUMMY_USERS

DB_FILE = 'database.db'

def init_db():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Create tables
    c.execute(CREATE_USERS_TABLE)
    c.execute(CREATE_QUARTERS_TABLE)

    # Insert dummy users
    c.executemany('INSERT INTO users (user_id, username, password) VALUES (?, ?, ?)', DUMMY_USERS)

    conn.commit()
    conn.close()
