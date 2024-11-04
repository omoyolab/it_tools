import sqlite3

def ingest_log(data):
    conn = sqlite3.connect('../database/logs.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (timestamp, source, severity, message) VALUES (?, ?, ?, ?)",
                   (data['timestamp'], data['source'], data['severity'], data['message']))
    conn.commit()
    conn.close()
