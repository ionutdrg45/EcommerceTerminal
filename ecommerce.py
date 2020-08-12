import os

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []
    
    prd_found = 0 # product found in products list
    prc_found = 0 # purchase found in purchases list
    prc_costs = 0 # purchases costs

    def purchase(self, inventory, product, products):
        for prd in products:
            if prd.name == product:
                self.prd_found = 1
                inventory_dict = inventory.inventory
                if prd in inventory_dict:
                    if inventory_dict[prd] > 0:
                        self.purchases.append(prd)
                        inventory_dict[prd] -= 1
                        print("You purchased {} that cost {}".format(prd.name, str(prd.price)))
                    else:
                        print('We are out of stock!')
                else:
                    print('We don\'t have that product!')
        if self.prd_found == 0:
            print("We don't have that product!")

    def print_purchases(self):
        for item in self.purchases:
            print(item.name)
            self.prc_found = 1
            self.prc_costs += item.price
        if self.prc_found == 0:
            print("You don't have any purchases!")
        else:
            print("Total: {}".format(str(self.prc_costs)))

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else :
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ": " + str(value) + " available")
        print()

inventory = Inventory()

def print_commands():
    os.system('cls')
    print("Use /help whenever you want to view the commands")
    print("/inventory - with this command you will see store inventory")
    print("/purchase - with this command you will see store inventory")
    print("/purchases - show your purchases")
    print("/q - quit")
    print()

customer = Customer(input("Hello! Type your name: "), input("Great! Now type your email address: "))

products = [Product('Apple watch', 299), Product('Mac', 1999), Product('Laptop', 1000)]

inventory = Inventory()
inventory.add_product(products[0], 100)
inventory.add_product(products[1], 100)
inventory.add_product(products[2], 100)

print_commands()

choice = input("command: ")

while choice != "/q":
    if choice == "/inventory":
        os.system('cls')
        inventory.print_inventory()
    elif choice == "/purchase":
        os.system('cls')
        customer.purchase(inventory, input("Please enter product: "), products)
    elif choice == "/purchases":
        os.system('cls')
        customer.print_purchases()
    elif choice == "/help":
        os.system('cls')
        print_commands()
    choice = input("command: ")

