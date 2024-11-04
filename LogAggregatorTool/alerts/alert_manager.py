from backend.db_setup import fetch_logs

alert_conditions = []

def set_alert_condition(condition):
    """Sets a new alert condition."""
    alert_conditions.append(condition)

def check_alerts(log_entry):
    """Checks a log entry against alert conditions."""
    triggered_alerts = []
    for condition in alert_conditions:
        if condition["keyword"] in log_entry["message"] and log_entry["severity"] == condition["severity"]:
            triggered_alerts.append(condition)
    return triggered_alerts
