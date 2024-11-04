import psutil

def get_network_status():
    network_io = psutil.net_io_counters()
    return {"bytes_sent": network_io.bytes_sent, "bytes_received": network_io.bytes_recv}
