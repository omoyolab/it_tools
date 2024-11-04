# Log Aggregator and Analyzer

## Overview
The Log Aggregator and Analyzer tool collects logs from multiple sources (e.g., Syslog, Windows Event Logs) and centralizes them for easy viewing, filtering, and alerting. This tool provides a dashboard for real-time monitoring and analysis of log data.

## Features
- **Centralized Log Storage**: Collects logs from Syslog and Windows Event Logs.
- **Log Filtering and Search**: Allows filtering by keyword, severity, or source.
- **Alerting System**: Sends notifications based on configured alert conditions.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/omoyolab/LogAggregatorTool.git
   cd LogAggregatorTool
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Database:**
   ```bash
   python backend/db_setup.py
   ```

4. **Run the Application:**
   ```bash
   python backend/app.py
   ```

## Configuration
- **Syslog Forwarding**: Configure `syslog.conf` to forward logs to the aggregator.
- **Windows Event Logs**: Use `windows_event.conf` for event log forwarding.

## Usage
1. Open the web dashboard at `http://localhost:5000`.
2. Use the interface to filter logs, set alerts, and view real-time log data.

---

## File Structure
- `backend/`: Contains the backend API, database setup, and log ingestion scripts.
- `frontend/`: HTML, CSS, and JavaScript files for the web interface.
- `database/`: SQLite database files for log storage.
- `config/`: Config files for log sources.
- `alerts/`: Logic for managing and sending alerts.

## Future Improvements
- Support for additional log sources.
- Enhanced filtering and search functionality.
- Integration with external alerting tools.

## License
This project is licensed under the MIT License.
