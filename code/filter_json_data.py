import csv

def filter_products_by_price(file_path, min_price):
    """Filters products by price greater than min_price."""
    filtered_data = []

    # Open and read the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Filter the rows based on the price column
        for row in reader:
            try:
                if float(row['Price']) > min_price:
                    filtered_data.append(row)
            except ValueError:
                # Skip rows where price is not a valid number
                continue
                
    return filtered_data

def write_filtered_data(file_path, filtered_data):
    """Writes the filtered data to a new CSV file."""
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['Name', 'Price', 'Category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()
        # Write the filtered rows
        writer.writerows(filtered_data)

if __name__ == "__main__":
    input_file_path = '../data/products.csv'  # Path to the input CSV
    output_file_path = '../output/filtered_products.csv'  # Path to the output CSV

    min_price = 100  # Minimum price to filter products

    # Filter the products by price
    filtered_data = filter_products_by_price(input_file_path, min_price)
    
    # Write the filtered data to a new CSV file
    write_filtered_data(output_file_path, filtered_data)
    
    print(f"Filtered products with price greater than {min_price} are saved in {output_file_path}")
