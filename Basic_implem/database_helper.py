import asyncio
import aiosqlite
import sqlite3

db_file = 'database.db'

def update_val(id, val):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Data SET value = ? WHERE id = ?
    ''', (val,id))

def insert_location(location, value):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Data (location, value) VALUE (?, ?)
    ''', (location, value))

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
