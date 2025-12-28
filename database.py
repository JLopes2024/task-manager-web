import sqlite3

def get_connection():
    conn = sqlite3.connect("tasks.db")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()
