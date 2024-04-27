class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break

    def update_quantity(self, product_name, new_quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity = new_quantity
                break

    def display_products(self):
        for product in self.products:
            print(f"Product Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

# Пример использования
warehouse = Warehouse()

product1 = Product("Apple", 1.50, 100)
product2 = Product("Banana", 0.75, 200)

print(product1)