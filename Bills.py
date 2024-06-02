class Store:
    def __init__(self):
        self.products = []

    def add_product(self, code, name, price):
        product = {'code': code, 'name': name, 'price': price}
        self.products.append(product)

    def display_menu(self):
        print('Product Menu:')
        for product in self.products:
            print(f"Code: {product['code']} | Name: {product['name']} | Price: {product['price']}")

    def generate_bill(self, codes):
        total = 0
        for code in codes:
            product = [p for p in self.products if p['code'] == code]
        if product:
            total += product[0]['price']
        return total

store = Store()
store.add_product(1, 'Pen', 10)
store.add_product(2, 'Soap', 20)
store.add_product(3, 'Book', 50)
store.add_product(4, 'NoteBook', 40)
store.add_product(5, 'Pencil Box', 20)
store.display_menu()
bill = store.generate_bill([1, 2, 3, 4, 5])
print("Total bill amount:", bill)