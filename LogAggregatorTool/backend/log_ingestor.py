import socket
from datetime import datetime
from backend.db_setup import insert_log

def start_syslog_listener(host="0.0.0.0", port=514):
    """Starts a UDP listener to receive Syslog messages."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"Syslog listener started on {host}:{port}")

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode("utf-8")
        log_entry = {
            "timestamp": datetime.now(),
            "source": addr[0],
            "severity": "info",  # Could parse severity from message if needed
            "message": message
        }
        insert_log(log_entry)

# Run this listener in a separate thread when starting the app
