class Frendika:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}"

class ProductService:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break

    def update_product(self, product_name, new_price, new_stock):
        for product in self.products:
            if product.name == product_name:
                product.price = new_price
                product.stock = new_stock
                break

def main():
    products = []
    product_service = ProductService(products)

    for i in range(2):
        name = input(f"Masukkan nama produk {i+1}: ")
        price = int(input(f"Masukkan harga produk {i+1}: "))
        stock = int(input(f"Masukkan jumlah stok produk {i+1}: "))
        product = Frendika(name, price, stock)
        product_service.add_product(product)

    for product in products:
        print(product)

if __name__ == "__main__":
    main()