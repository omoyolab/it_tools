from flask import Flask, request, jsonify
from backend.log_ingestor import ingest_log
from alerts.alert_manager import check_alerts

app = Flask(__name__)

@app.route('/')  # Add a root route
def home():
    return "Welcome to the Log Aggregator Tool!"

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    ingest_log(data)
    check_alerts(data)
    return jsonify({"status": "log ingested"}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    # Logic to fetch logs from database
    return jsonify({"logs": []}), 200

@app.route('/alerts', methods=['POST'])
def set_alert():
    # Logic to configure alert condition
    return jsonify({"status": "alert configured"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Ensuring it's accessible on port 8000
