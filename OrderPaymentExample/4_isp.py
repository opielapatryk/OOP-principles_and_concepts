# Interface Segregation Principle (ISP)
# The Interface Segregation Principle states that clients should not be forced to depend on methods they do not use. This means that you should not have to implement methods that you do not need.

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

class SmsAuthorizer:
    def __init__(self):
        self.autheticated = False

    def verify_code(self,code: str):
        print("verifying")
        self.autheticated = True
    
    def is_auth(self):
        return self.autheticated


class CreditCardProcessorPayment(PaymentProcessor):
     def __init__(self, security_code: str) -> None:
         self.security_code = security_code

     def pay(self, order: Order):
          print("Processing credit card")
          print(f"Verifying scurity code: {self.security_code}")
          order.status = "paid"
    

class DebitCardProcessorPayment():
     def __init__(self, security_code: str, authorizer: SmsAuthorizer) -> None:
         self.security_code = security_code
         self.authorizer = authorizer

     def pay(self, order: Order):
          if not self.authorizer.is_auth():
              raise Exception("Not authenticated")
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
auth = SmsAuthorizer()
auth.verify_code('123123')
processor = DebitCardProcessorPayment("4234234",auth)
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
processor.pay(order)
