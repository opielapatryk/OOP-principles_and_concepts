# Single Responsibility Principle (SRP)
# It should do one thing and do it well. By adhering to SRP, your code becomes more modular, making it easier to understand and maintain.

class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

class PaymentProcessor:
    def pay(self, order: Order, security_code):
            print("Processing payment")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"


order = Order()
processor = PaymentProcessor()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
processor.pay(order, "0372846")
