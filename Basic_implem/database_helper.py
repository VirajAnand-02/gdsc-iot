import asyncio
import aiosqlite
import sqlite3

db_file = 'database.db'

def init_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            value TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRNET_TIMESTAMP
        )
    ''')