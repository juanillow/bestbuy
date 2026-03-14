class Product:
    """Represents a product in the store"""

    def __init__(self, name, price, quantity):
        """Initialize product data and default active state"""
        if name == "":
            raise Exception("Name cannot be empty")
        if price < 0:
            raise Exception("Price cannot be negative")
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return current product quantity"""
        return self.quantity

    def set_quantity(self, quantity):
        """Set quantity and update active status"""
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self):
        """Return True if product is active"""
        return self.active

    def activate(self):
        """Activate the product"""
        self.active = True

    def deactivate(self):
        """Deactivate the product"""
        self.active = False

    def show(self):
        """Print product details"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Buy units and return total purchase price"""
        if quantity <= 0:
            raise Exception("Quantity to buy must be positive")
        if not self.active:
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


def main():
    """Run a basic Product usage example"""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
