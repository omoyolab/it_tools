import sqlite3

def check_alerts(data):
    conn = sqlite3.connect('../database/logs.db')
    cursor = conn.cursor()
    # Check for alert conditions based on severity or keywords
    if "error" in data['message'].lower():
        # Logic to send an alert, e.g., email or notification
        print("Alert triggered:", data)
    conn.close()
