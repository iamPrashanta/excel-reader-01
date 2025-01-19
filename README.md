# README

## Introduction
This project processes an Excel file to filter and calculate data based on specific conditions, and provides a web interface using Flask to display results and download files.

---

## Setup Instructions

### Installing Required Packages
To run this project, you need to install the following Python packages:

1. **Pandas** (for data manipulation and Excel file handling)
   ```bash
   pip install pandas
   ```

2. **Flask** (for creating a web interface)
   ```bash
   pip install flask
   ```

3. **OpenPyXL** (for working with Excel files if not already installed)
   ```bash
   pip install openpyxl
   ```

### Attaching Your Excel File
1. Place your Excel file in the project directory.
2. Update the `file_path` variable in the script to the path of your Excel file:
   ```python
   file_path = 'path_to_your_excel_file.xlsx'
   ```

### Excel Table Headers
The Excel file should have the following main headers:
- **amount**: The column containing numeric values to be filtered and summed.
- **insert_date**: The column containing date and time values for filtering by a specific range.
- **status**: The column containing transaction status, e.g., "Transaction Successfull."

---

## Functionality Details

### Why Use Max Length for Amount
To ensure data quality and eliminate potentially invalid entries, the script filters out rows where the length of the value in the "amount" column exceeds 5 characters. This prevents outliers or unexpected large values from affecting the results.

### Filtering Using Date
The script filters rows based on a specified date range using the "insert_date" column. Only rows within the provided start and end dates are included in the calculations.

### Filtering Using Status
Rows with a "status" column value other than "Transaction Successfull" are ignored and saved into a separate Excel file (`ignored_rows.xlsx`).

---

## Changing Port if Already Running
If the default Flask port (5000) is already in use, change the port in the script as follows:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to an available port
```

---

## Output Files
1. **filtered_data.xlsx**: Contains rows that meet all filtering conditions (amount length, date range, and status).
2. **ignored_rows.xlsx**: Contains rows ignored due to exceeding the maximum length for "amount" or having an invalid "status."

---

## Running the Application
1. Run the script:
   ```bash
   python script_name.py
   ```
2. Open a web browser and navigate to `http://127.0.0.1:5000` to view results and download files.

---

## Notes
- Ensure your Excel file adheres to the required column structure.
- Always validate the output files to ensure accuracy in filtering and calculations.

