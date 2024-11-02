document.getElementById('compareButton').addEventListener('click', compareFiles);

function compareFiles() {
    const workingFile = document.getElementById('workingFile').files[0];
    const nonWorkingFile = document.getElementById('nonWorkingFile').files[0];

    if (!workingFile || !nonWorkingFile) {
        alert("Please upload both files.");
        return;
    }

    Promise.all([readFile(workingFile), readFile(nonWorkingFile)]).then(filesContent => {
        const parser = new DOMParser();
        const workingDoc = parser.parseFromString(filesContent[0], "text/html");
        const nonWorkingDoc = parser.parseFromString(filesContent[1], "text/html");

        const workingData = extractGPSettings(workingDoc);
        const nonWorkingData = extractGPSettings(nonWorkingDoc);

        displayDifferences(workingData, nonWorkingData);
    });
}

function readFile(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = () => reject(reader.error);
        reader.readAsText(file);
    });
}

function extractGPSettings(doc) {
    const settings = {};
    const rows = doc.querySelectorAll("table tr"); // Adjust selector based on GP HTML structure

    rows.forEach(row => {
        const cells = row.querySelectorAll("td");
        if (cells.length === 2) {
            const key = cells[0].textContent.trim();
            const value = cells[1].textContent.trim();
            settings[key] = value;
        }
    });

    return settings;
}

function displayDifferences(workingData, nonWorkingData) {
    const resultBody = document.getElementById('resultBody');
    resultBody.innerHTML = ''; // Clear previous results

    const allKeys = new Set([...Object.keys(workingData), ...Object.keys(nonWorkingData)]);
    allKeys.forEach(key => {
        const workingValue = workingData[key] || 'N/A';
        const nonWorkingValue = nonWorkingData[key] || 'N/A';

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${key}</td>
            <td>${workingValue}</td>
            <td class="${workingValue !== nonWorkingValue ? 'diff' : ''}">${nonWorkingValue}</td>
        `;
        resultBody.appendChild(row);
    });
}
