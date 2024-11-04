# Information Technology Tools

[![Deploy GP Result Static Files](https://github.com/omoyolab/it_tools/actions/workflows/deploy_GPResult.yml/badge.svg)](https://github.com/omoyolab/it_tools/actions/workflows/deploy_GPResult.yml)  
[![Deploy Browser Policy Static Files](https://github.com/omoyolab/it_tools/actions/workflows/deploy_browserPolicy.yml/badge.svg)](https://github.com/omoyolab/it_tools/actions/workflows/deploy_browserPolicy.yml)

This repository contains tools that can be used for day-to-day IT tasks by system admins and IT administrators.

---

## Author
Developed collaboratively by Abimbola Omoyola and contributors.

---

## Tools

| Tool Name               | URL                                                                 |
|-------------------------|---------------------------------------------------------------------|
| GPDiffChecker           | [GPDiffChecker](https://icy-hill-03c198f10.5.azurestaticapps.net/) |
| BrowserPolicyDiffChecker| [BrowserPolicyDiffChecker](https://salmon-ground-01423c410.5.azurestaticapps.net/) |
| CommandHelper           | Local Batch File                                                   |
| Log Aggregator and Analyzer | Local Tool                                                     |

---

## Tool Descriptions

### GPDiffChecker
**URL:** [GPDiffChecker](https://icy-hill-03c198f10.5.azurestaticapps.net/)  
The GPDiffChecker tool allows IT administrators to upload working and non-working Group Policy (GP) result files in HTML format. It provides a detailed comparison, highlighting the differences between the two files, which can be especially useful for troubleshooting and identifying specific policy discrepancies. This tool is particularly valuable for understanding variances in applied policies across systems.

### BrowserPolicyDiffChecker
**URL:** [BrowserPolicyDiffChecker](https://salmon-ground-01423c410.5.azurestaticapps.net/)  
The BrowserPolicyDiffChecker tool is designed to help administrators compare browser policy JSON files. By displaying differences between two policy files, this tool assists in understanding changes and identifying potential issues within browser configurations. The tool is an asset for IT administrators managing browser settings and policies across an organization.

### CommandHelper
**Local Batch File**  
The CommandHelper tool is a batch file providing a menu-driven interface for system cleanup tasks, particularly focused on clearing various types of browser data. It includes options to delete:

- Non-trusted web history
- Browsing history
- Cookies
- Temporary internet files
- Form data
- Stored passwords
- Comprehensive cleanup of all data types

This tool is valuable for administrators needing to perform quick browser data management and cleanup across Windows systems, streamlining these routine tasks.

### Log Aggregator and Analyzer
**Local Tool**  
The Log Aggregator and Analyzer tool collects logs from multiple sources, such as Syslog and Windows Event Logs, and centralizes them for easy viewing, filtering, and alerting. It provides a dashboard for real-time monitoring and analysis of log data.

#### Features
- **Centralized Log Storage**: Collects logs from Syslog and Windows Event Logs.
- **Log Filtering and Search**: Allows filtering by keyword, severity, or source.
- **Alerting System**: Sends notifications based on configured alert conditions.

#### Setup and Usage
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
