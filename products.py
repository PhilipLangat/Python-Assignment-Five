import csv
import os

# File path for storing products
PRODUCTS_FILE = "products.csv"

# Ensure the CSV file exists
def ensure_file_exists():
    if not os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Price', 'Quantity'])  # Header for the CSV file

# Add a product
def add_product():
    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        with open(PRODUCTS_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, price, quantity])
        print("Product added successfully!")
    except ValueError:
        print("Error: Invalid price or quantity. Please enter numeric values.")

# View all products
def view_products():
    try:
        with open(PRODUCTS_FILE, 'r') as file:
            reader = csv.reader(file)
            products = list(reader)
            if len(products) > 1:
                print("\nProduct List:")
                print(f"{'Name':<15} {'Price':<10} {'Quantity':<10}")
                for product in products[1:]:
                    print(f"{product[0]:<15} {product[1]:<10} {product[2]:<10}")
            else:
                print("No products available.")
    except FileNotFoundError:
        print("Error: Products file not found.")

# Update a product
def update_product():
    try:
        name = input("Enter the name of the product to update: ")
        found = False
        products = []
        
        with open(PRODUCTS_FILE, 'r') as file:
            reader = csv.reader(file)
            products = list(reader)

        for i, product in enumerate(products):
            if product[0].lower() == name.lower():
                found = True
                try:
                    new_price = float(input(f"Enter new price for {product[0]}: "))
                    new_quantity = int(input(f"Enter new quantity for {product[0]}: "))
                    products[i] = [product[0], new_price, new_quantity]
                    break
                except ValueError:
                    print("Error: Invalid price or quantity.")
                    return

        if found:
            with open(PRODUCTS_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
            print("Product updated successfully!")
        else:
            print("Product not found.")
    except FileNotFoundError:
        print("Error: Products file not found.")

# Delete a product
def delete_product():
    try:
        name = input("Enter the name of the product to delete: ")
        found = False
        products = []

        with open(PRODUCTS_FILE, 'r') as file:
            reader = csv.reader(file)
            products = list(reader)

        for i, product in enumerate(products):
            if product[0].lower() == name.lower():
                found = True
                del products[i]
                break

        if found:
            with open(PRODUCTS_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
            print("Product deleted successfully!")
        else:
            print("Product not found.")
    except FileNotFoundError:
        print("Error: Products file not found.")

# Main menu function
def menu():
    ensure_file_exists()  # Ensure the CSV file exists when the program starts
    while True:
        print("\nProduct Management System")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()
