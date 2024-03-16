import csv
import json
import os

# Example usage:
directory_path = 'C:\\Users\\saini\\data'

# Ensure the directory path ends with a '/'
directory = directory_path.rstrip('/') + '/'

# List all files in the directory
files = os.listdir(directory)


# Iterate through each file in the directory
for file_name in files:
    if file_name.endswith('.csv'):
        csv_file_path = directory + file_name
        json_file_path = directory + file_name.replace('.csv', '.json')

        with open(csv_file_path, 'r') as csv_file:
            # Read CSV file
            csv_data = csv.DictReader(csv_file)
            # Convert CSV data to a list of dictionaries
            data = [row for row in csv_data]

        # Write JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

        print(f"Converted: {file_name} -> {file_name.replace('.csv', '.json')}")


