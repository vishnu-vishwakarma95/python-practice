import csv

def read_csv(file_path):
    """Reads the CSV file and returns the data as a list of rows."""
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def calculate_column_averages(data):
    """Calculates averages for each column."""
    num_columns = len(data[0])
    averages = []
    
    for col in range(1, num_columns):  # Skip the first column (Name)
        column_values = [float(row[col]) for row in data[1:] if row[col].replace('.', '', 1).isdigit()]
        column_average = sum(column_values) / len(column_values) if column_values else 0
        averages.append(column_average)
    
    return averages

def write_averages(file_path, averages):
    """Writes the column averages to a new CSV file."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Average'] + averages)

if __name__ == "__main__":
    data = read_csv('../data/data.csv')  # Path to the CSV file
    averages = calculate_column_averages(data)
    write_averages('../output/averages.csv', averages)
    print("Averages calculated and written to averages.csv")
