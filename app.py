import os
import sys
import psycopg2

class Shop:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                               id SERIAL PRIMARY KEY,
                               name TEXT NOT NULL,
                               price REAL NOT NULL)''')
        self.connection.commit()

    def add_product(self, name, price):
        self.cursor.execute('''INSERT INTO products (name, price) VALUES (%s, %s)''', (name, price))
        self.connection.commit()

    def remove_product(self, product_id):
        self.cursor.execute('''DELETE FROM products WHERE id = %s''', (product_id,))
        self.connection.commit()

    def list_products(self):
        self.cursor.execute('''SELECT * FROM products''')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    shop = Shop()

    while True:
        try:
            print("\n1. Add Product")
            print("2. Remove Product")
            print("3. List Products")
            print("4. Exit")

            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                shop.add_product(name, price)
            elif choice == "2":
                product_id = int(input("Enter product ID to remove: "))
                shop.remove_product(product_id)
            elif choice == "3":
                products = shop.list_products()
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
            elif choice == "4":
                print("Exiting...")
                shop.close()
                break
            else:
                print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            shop.close()
            break
