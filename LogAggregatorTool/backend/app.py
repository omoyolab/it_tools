from flask import Flask, request, jsonify
from log_ingestor import ingest_log
from alert_manager import check_alerts

app = Flask(__name__)

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
    # Logic to configure alert conditions
    return jsonify({"status": "alert configured"}), 200

if __name__ == '__main__':
    app.run(debug=True)
