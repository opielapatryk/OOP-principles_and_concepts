# Open-Closed Principle (OCP)
# The Open-Closed Principle states that software entities should be open for extension but closed for modification. This means that you should be able to extend a class’s behavior without modifying it.
from abc import ABC, abstractmethod

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

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order, security_code: str):
            print("Processing payment")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"

class CreditCardProcessorPayment(PaymentProcessor):
     def pay(self, order: Order, security_code: str):
          print("Processing credit card")
          print(f"Verifying security code: {security_code}")
          order.status = "paid"

class DebitCardProcessorPayment(PaymentProcessor):
     def pay(self, order: Order, security_code: str):
          print("Processing debit card")
          print(f"Verifying security code: {security_code}")
          order.status = "paid"

class PaypalProcessorPayment(PaymentProcessor):
     def pay(self, order: Order, security_code: str):
          print("Processing paypal")
          print(f"Verifying security code: {security_code}")
          order.status = "paid"


order = Order()
processor = CreditCardProcessorPayment()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
processor.pay(order, "0372846")
