# Liskov Substitution Principle (LSP)
# The Liskov Substitution Principle states that objects in a program should be replaceable with instances of their subtypes without altering the correctness of the program. In other words, a subclass should be able to replace its parent class without breaking the code.

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
    def pay(self, order: Order):
        pass

class CreditCardProcessorPayment(PaymentProcessor):
     def __init__(self, security_code: str) -> None:
         self.security_code = security_code

     def pay(self, order: Order):
          print("Processing credit card")
          print(f"Verifying scurity code: {self.security_code}")
          order.status = "paid"

class DebitCardProcessorPayment(PaymentProcessor):
     def __init__(self, security_code: str) -> None:
         self.security_code = security_code

     def pay(self, order: Order):
          print("Processing debit card")
          print(f"Verifying scurity code: {self.security_code}")
          order.status = "paid"

class PaypalProcessorPayment(PaymentProcessor):
     def __init__(self, email_address: str) -> None:
         self.email_address = email_address

     def pay(self, order: Order):
          print("Processing paypal")
          print(f"Verifying email address: {self.email_address}")
          order.status = "paid"


order = Order()
processor = PaypalProcessorPayment('patryk.opiela@gmail.com')
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
processor.pay(order)
