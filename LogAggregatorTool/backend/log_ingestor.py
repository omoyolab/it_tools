import socket
from datetime import datetime
from backend.db_setup import insert_log

def start_syslog_listener(host="0.0.0.0", port=5566):  # Updated to port 5566
    """Starts a UDP listener to receive Syslog messages."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind((host, port))
        print(f"Syslog listener started on {host}:{port}")
    except OSError as e:
        print(f"Error: {e}. Port {port} may be in use. Try a different port.")
        return  # Exit if binding fails

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode("utf-8")
        log_entry = {
            "timestamp": datetime.now(),
            "source": addr[0],
            "severity": "info",
            "message": message
        }
        insert_log(log_entry)



def ingest_log(data):
    """Processes incoming log data."""
    log_entry = {
        "timestamp": data.get("timestamp", datetime.now()),
        "source": data.get("source", "unknown"),
        "severity": data.get("severity", "info"),
        "message": data.get("message", "")
    }
    insert_log(log_entry)
