document.getElementById('compareButton').addEventListener('click', compareFiles);

function compareFiles() {
    const workingFile = document.getElementById('workingFile').files[0];
    const nonWorkingFile = document.getElementById('nonWorkingFile').files[0];

    if (!workingFile || !nonWorkingFile) {
        alert("Please upload both JSON files.");
        return;
    }

    Promise.all([readFile(workingFile), readFile(nonWorkingFile)]).then(filesContent => {
        const workingData = JSON.parse(filesContent[0]);
        const nonWorkingData = JSON.parse(filesContent[1]);

        const workingPolicies = workingData.policyValues.chrome.policies || {};
        const nonWorkingPolicies = nonWorkingData.policyValues.chrome.policies || {};

        displayDifferences(workingPolicies, nonWorkingPolicies);
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

function displayDifferences(workingPolicies, nonWorkingPolicies) {
    const resultBody = document.getElementById('resultBody');
    resultBody.innerHTML = ''; // Clear previous results

    const allKeys = new Set([...Object.keys(workingPolicies), ...Object.keys(nonWorkingPolicies)]);
    
    allKeys.forEach(key => {
        const workingValue = JSON.stringify(workingPolicies[key]?.value) || 'N/A';
        const nonWorkingValue = JSON.stringify(nonWorkingPolicies[key]?.value) || 'N/A';

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${key}</td>
            <td>${workingValue}</td>
            <td class="${workingValue !== nonWorkingValue ? 'diff' : ''}">${nonWorkingValue}</td>
        `;
        resultBody.appendChild(row);
    });
}
