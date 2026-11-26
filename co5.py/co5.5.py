import csv

csv_col = ['ID', 'Name', 'Country']  # Column names (Header)

# Dictionary data
dict_data = [
    {'ID': 1, 'Name': 'Alex', 'Country': 'India'},
    {'ID': 2, 'Name': 'Aleena', 'Country': 'India'},
    {'ID': 3, 'Name': 'Minu', 'Country': 'UK'},
    {'ID': 4, 'Name': 'Ebin', 'Country': 'USA'},
    {'ID': 5, 'Name': 'Jimmy', 'Country': 'India'}
]

csv_file1 = "Names.csv"  # CSV file name

# Writing dictionary data into CSV file
with open(csv_file1, 'w', newline='') as file1:
    writer = csv.DictWriter(file1, fieldnames=csv_col)
    writer.writeheader()  # Write column headings

    for data1 in dict_data:
        writer.writerow(data1)

print("Data successfully written to CSV file.")

# Reading the CSV file
with open(csv_file1, 'r', newline='') as file1:
    reader = csv.DictReader(file1)

    print("\nCSV file as a dictionary:\n")

    for row in reader:
        print(row)
