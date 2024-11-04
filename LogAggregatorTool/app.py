import threading
from flask import Flask, request, jsonify, render_template
from backend.log_ingestor import start_syslog_listener, ingest_log  # Ensure ingest_log is imported
from alerts.alert_manager import check_alerts, set_alert_condition
from backend.db_setup import fetch_logs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Renders the HTML template

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    ingest_log(data)  # Process the log data
    alerts = check_alerts(data)
    if alerts:
        return jsonify({"status": "log ingested", "alerts": alerts}), 200
    return jsonify({"status": "log ingested"}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = fetch_logs()
    return jsonify({"logs": logs}), 200

@app.route('/alerts', methods=['POST'])
def set_alert():
    condition = request.json  # Expects {"keyword": "error", "severity": "high"}
    set_alert_condition(condition)
    return jsonify({"status": "alert condition set"}), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    # Placeholder for actual metrics
    return jsonify({"status": "metrics endpoint active"}), 200

if __name__ == '__main__':
    # Start the Syslog listener in a background thread
    syslog_thread = threading.Thread(target=start_syslog_listener, args=("0.0.0.0", 515))  # Change port if needed
    syslog_thread.daemon = True
    syslog_thread.start()

    app.run(debug=True, host='0.0.0.0', port=8000)
