document.addEventListener('DOMContentLoaded', () => {
    fetchLogs();
});

function fetchLogs() {
    fetch('/logs')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('log-container');
            data.logs.forEach(log => {
                const logEntry = document.createElement('div');
                logEntry.textContent = `${log.timestamp} - ${log.source}: ${log.message}`;
                container.appendChild(logEntry);
            });
        });
}
