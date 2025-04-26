# app/database/dummy_data.py

from app.utils.security import hash_password

DUMMY_USERS = [
    (1001, 'Vishal', hash_password('vishal123')),
    (1002, 'Kunal', hash_password('kunal123')),
    (1003, 'Ajay', hash_password('ajay123')),
    (1004, 'Rohit', hash_password('rohit123')),
    (1005, 'Keshav', hash_password('keshav123')),
]
