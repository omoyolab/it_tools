import sqlite3

def setup_database():
    conn = sqlite3.connect('../database/logs.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        source TEXT,
        severity TEXT,
        message TEXT
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT,
        severity TEXT,
        action TEXT
    )''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
