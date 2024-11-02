# Machine Group Policy JSON Diff Checker

This is a simple web tool for comparing Machine Group policy files and displaying differences between a "Working" and "Non-Working" configuration.

## Features
- Upload two Group policy html files and compare them.
- Display differences in policy values.
- Highlight differences in a table format.

## Setup and Deployment

This project is hosted on Azure Static Web Apps. It uses GitHub Actions for CI/CD to automatically deploy changes pushed to the `master` branch.

### File Structure

- `assets/index.html`: The main HTML structure.
- `assets/script.js`: Contains the JavaScript logic to read, parse, and compare JSON files.
- `assets/style.css`: Basic styling for the web tool.
- `.github/workflows/deploy.yml`: GitHub Actions configuration for CI/CD.

### Running Locally
You can open the `assets/index.html` file directly in your browser to use this tool locally.

### Deployment Instructions

1. **GitHub Setup**:
   - Ensure your GitHub repository has the secret `AZURE_STATIC_WEB_APPS_API_TOKEN` for deploying to Azure Static Web Apps.
   - Push your changes to the `master` branch for automatic deployment.

2. **Azure Setup**:
   - [Create an Azure Static Web App](https://portal.azure.com/), link it to your GitHub repository, and obtain the API token for deployment.

## License
MIT License
