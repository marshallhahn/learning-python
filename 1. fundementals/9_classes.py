class CoffeeShop:
    # Constructor
    def __init__(self, address, menu) -> None:
        self.address = address
        self.menu = menu

    # Directions method
    def get_directions(self):
        return self.address

    # Add menu item method
    def add_menu_item(self, item):
        self.menu.append(item)
        return self.menu


# Create instance of the coffee shop class
valor_coffee = CoffeeShop(
    address="1234 Main Street", menu=["drip", "latte", "espresso"]
)

# Print the address
print(valor_coffee.get_directions())

# Print the menu
print(valor_coffee.menu)

# Add an item to the menu
valor_coffee.add_menu_item("cappuccino")
print(valor_coffee.menu)
