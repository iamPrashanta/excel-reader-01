import pandas as pd
from flask import Flask, render_template_string
# Flask app setup
app = Flask(__name__)

# File path for the Excel file
file_path = 'your-excel-file.xlsx'
# Parameters for filtering
search = 'amount'
max_length = 6
date_column = 'insert_date'
status_column = 'status'
status_value = 'Transaction Successfull'
start_date = '2024-02-01 00:00:01'
end_date = '2024-08-31 23:59:59'

# Read the Excel file
data = pd.read_excel(file_path)

# Check if required columns are present
if search in data.columns and date_column in data.columns and status_column in data.columns:
    # Convert 'amount' column to string and filter by length
    data[search] = data[search].astype(str)
    ignored_rows = data[data[search].str.len() > max_length]

    # Include rows where status is not 'Transaction Successfull' in ignored rows
    ignored_status_rows = data[data[status_column] != status_value]
    ignored_rows = pd.concat([ignored_rows, ignored_status_rows]).drop_duplicates()
    ignored_rows_count = len(ignored_rows)

    filtered_data = data[(data[search].str.len() <= max_length) & (data[status_column] == status_value)].copy()

    # Convert 'amount' column back to numeric
    filtered_data[search] = pd.to_numeric(filtered_data[search], errors='coerce')

    # Filter by date range
    filtered_data[date_column] = pd.to_datetime(filtered_data[date_column], errors='coerce')
    filtered_data = filtered_data[
        (filtered_data[date_column] >= pd.to_datetime(start_date)) & (
                    filtered_data[date_column] <= pd.to_datetime(end_date))
        ]

    # Calculate the total amount
    total_amount = filtered_data[search].sum()

    # Save the filtered data to a new Excel file
    # output_file = 'filtered_data.xlsx'
    # filtered_data.to_excel(output_file, index=False)

    # Save the ignored rows to a separate Excel file
    ignored_rows_file = 'ignored_rows.xlsx'
    ignored_rows.to_excel(ignored_rows_file, index=False)

    # Flask route to display results
    @app.route('/')
    def display_results():
        html_template = f"""
            <html>
                <head><title>Filtered Data Results</title></head>
                <body>
                    <h1>Data Processing Results</h1>
                    <p>Total Amount (excluding rows length > {max_length} and filtered by date/status): {total_amount}</p>
                    <p>Number of rows ignored due to 'amount' length > {max_length} or incorrect status: {ignored_rows_count}</p>
                    <p><a href="/{ignored_rows_file}" download>Download Ignored Rows</a></p>
                </body>
            </html>
            """
        return render_template_string(html_template)

    if __name__ == '__main__':
        app.run(debug=True, port=8001)
else:
    print("One or more required columns ('amount', 'insert_date', 'status') not found in the dataset.")
