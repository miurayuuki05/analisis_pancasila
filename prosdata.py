import os
import csv

# Define the dataset folder path
dataset_folder = "./dataset"  # Replace with your dataset folder path
output_csv = "dataset.csv"

# Initialize a list to store the processed data
data = []
counter = 1  # Start the numbering from this value

# Iterate over all files in the dataset folder
for file_name in os.listdir(dataset_folder):
    file_path = os.path.join(dataset_folder, file_name)
    
    # Check if it's a file
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            
            # Split the file content by ';'
            parts = content.split(';')
            
            # Append each part to the data list with a global row number
            for part in parts:
                part = part.strip()  # Clean up the text
                if part:  # Ignore empty parts
                    data.append([counter, part])
                    counter += 1  # Increment the global counter

# Write the data to a CSV file
with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write header row
    writer.writerow(['no', 'text'])
    
    # Write the rows of data
    writer.writerows(data)

print(f"CSV file '{output_csv}' has been created successfully.")
