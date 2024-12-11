import sqlite3

def get_connection():
    return sqlite3.connect("db/database.db")

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        description TEXT,
        due_date TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    """)
    connection.commit()
