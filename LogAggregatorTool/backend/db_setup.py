import sqlite3

# Connects to the database or creates it if it doesn't exist
conn = sqlite3.connect("log_aggregator.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    source TEXT,
    severity TEXT,
    message TEXT
)
''')
conn.commit()

def insert_log(log_entry):
    """Inserts a log entry into the logs table."""
    cursor.execute('''
    INSERT INTO logs (timestamp, source, severity, message)
    VALUES (?, ?, ?, ?)
    ''', (log_entry["timestamp"], log_entry["source"], log_entry["severity"], log_entry["message"]))
    conn.commit()

def fetch_logs():
    """Fetches all logs from the logs table."""
    cursor.execute("SELECT * FROM logs")
    return cursor.fetchall()
