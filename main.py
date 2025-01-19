import pandas as pd

# File path for the Excel file
file_path = 'test.xlsx'
# Parameters for filtering
search = 'amount'
date_column = 'insert_date'
status_column = 'status'
status_value = 'Transaction Successfull'
start_date = '2023-05-25 15:54:01'
end_date = '2023-05-25 16:32:38'

# Read the Excel file
data = pd.read_excel(file_path)

# Check if required columns are present
if search in data.columns and date_column in data.columns and status_column in data.columns:
    # Convert 'amount' column to string and filter by length
    data[search] = data[search].astype(str)
    ignored_rows = data[data[search].str.len() > 6]
    ignored_rows_count = len(ignored_rows)
    filtered_data = data[data[search].str.len() <= 6].copy()

    # Convert 'amount' column back to numeric
    filtered_data[search] = pd.to_numeric(filtered_data[search], errors='coerce')

    # Filter by date range
    filtered_data[date_column] = pd.to_datetime(filtered_data[date_column], errors='coerce')
    filtered_data = filtered_data[
        (filtered_data[date_column] >= pd.to_datetime(start_date)) & (filtered_data[date_column] <= pd.to_datetime(end_date))
    ]

    # Filter by status
    filtered_data = filtered_data[filtered_data[status_column] == status_value]

    # Calculate the total amount
    total_amount = filtered_data[search].sum()

    # Print the result
    print(f"Total Amount (excluding rows length > 5 and filtered by date/status): {total_amount}")
    print(f"Number of rows ignored due to 'amount' length > 6: {ignored_rows_count}")

    # Save the filtered data to a new Excel file
    # output_file = 'filtered_data.xlsx'
    # filtered_data.to_excel(output_file, index=False)
    # print(f"Filtered data saved to {output_file}")

    # Save the ignored rows to a separate Excel file
    ignored_rows_file = 'ignored_rows.xlsx'
    ignored_rows.to_excel(ignored_rows_file, index=False)
    print(f"Ignored rows saved to {ignored_rows_file}")
else:
    print("One or more required columns ('amount', 'insert_date', 'status') not found in the dataset.")
