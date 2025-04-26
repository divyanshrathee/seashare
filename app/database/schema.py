# app/database/schema.py

CREATE_USERS_TABLE = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
'''

CREATE_QUARTERS_TABLE = '''
CREATE TABLE quarters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    rank TEXT NOT NULL,
    name TEXT NOT NULL,
    contact TEXT NOT NULL,
    building TEXT NOT NULL,
    notice_period TEXT NOT NULL
)
'''
