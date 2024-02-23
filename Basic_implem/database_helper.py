import asyncio
import aiosqlite
import sqlite3

db_file = 'database.db'

def update_val(location, val):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Data SET value = ? WHERE location = ?
    ''', (val,location))

def insert_location(location, value):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # Define the SQL query to insert a new row into the Data table
    sql_query = '''
        INSERT INTO Data (location, value) VALUES (?, ?)
    '''
    # Execute the SQL query with the given location and value
    cursor.execute(sql_query, (location, value))
    # Commit the changes to the database
    conn.commit()
    # Close the database connection
    conn.close()

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
