import requests
import time
from monitor.cpu_monitor import get_cpu_usage
from monitor.memory_monitor import get_memory_usage
from monitor.disk_monitor import get_disk_usage
from monitor.network_monitor import get_network_status
import socket

# The central server's IP address and port
CENTRAL_SERVER_URL = "http://<central_server_ip>:8000/ingest"

def send_metrics_to_server():
    data = {
        "hostname": socket.gethostname(),
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "network": get_network_status()
    }
    # Send data to central server
    response = requests.post(CENTRAL_SERVER_URL, json=data)
    print(f"Sent metrics to central server: {response.status_code}")

if __name__ == '__main__':
    while True:
        send_metrics_to_server()
        time.sleep(10)  # Send metrics every 10 seconds
