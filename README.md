# Caldera Report Generator

This Python script allows users to convert JSON reports downloaded from Caldera into readable, formatted PDF documents. The script uses the ReportLab library to generate the reports.

## Prerequisites
- Python 3.x
- Access to Caldera JSON reports

## Installation
1. ### Clone the Repository  
    First, clone this repository to your local machine using:
 
    ```bash
    git clone https://github.com/marksowell/caldera-report-generator.git
    cd caldera-report-generator
    ```
2. ### Install Dependencies  
    Install the required Python package ReportLab which is used for generating PDF files:  
    ```bash
    pip install reportlab
    ```
## Usage
To generate a PDF report from a Caldera JSON report:
1. **Prepare Your JSON File**: Ensure that you have a Caldera JSON report saved locally. For example, `report.json`.
2. **Run the Script**: Use the following command to generate a PDF report. Replace `/path/to/your/report.json` with the path to your Caldera JSON report.
     
    ```bash
    python generate_report.py /path/to/your/report.json
    ```
    The script will generate a uniquely named PDF file in the current directory, incorporating the operation's name with the report generation's date and time.

## Output
The script dynamically creates a PDF document with a filename in the format `operation_name_caldera_report_YYYY_MM_DD_HHMMSS.pdf`. Each report includes:
- Host information such as hostname, username, and IP addresses.
- Details of executed commands, their status, and timings.

## Troubleshooting
- **Dependency Errors**: If you encounter errors related to missing packages, make sure you have run the `pip install reportlab` command correctly.
- **File Not Found**: Ensure the JSON path is correct and accessible to the script.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.
- **Bug Reports**: Issues are tracked as GitHub issues. Tag it as a bug and include as much detail as possible to replicate the issue.
- **Feature Requests**: Feel free to add feature requests by opening an issue. Tag it as a feature request.
## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/marksowell/caldera-report-generator/blob/main/LICENSE) file for details.
