# superclass
class Product:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return self.model + " @ " + str(self.price)

# extends product class
class Laptop(Product):
    # inherits Product's functions
    pass

class Router(Product):
    pass

class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product): self.products.append(product)

    def __str__(self):
        return ", ".join([str(p) for p in self.products])

class Warehouse:
    def __init__(self, laptops, routers):
        self.laptops = laptops
        self.routers = routers

warehouse = Warehouse([Laptop('mac', 1999)], [Router('netgate', 600)])

order = Order()
order.add_product(warehouse.laptops[0])
order.add_product(warehouse.routers[0])
print(order)
