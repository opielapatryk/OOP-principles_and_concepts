from abc import abstractmethod, ABC

class Account(ABC):
    @abstractmethod
    def deposit(self, amount: float) -> bool:
        """
        Deposits the given amount into the account
        """
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the given amount from the account
        """
        pass

    @abstractmethod
    def checkBalance(self) -> float:
        """
        Returns the current account balance.
        """
        pass

    @abstractmethod
    def transfer(self, recipient_account_number: str, amount: float) -> bool:
        """
        Transfers the given amount to the specified recipient account
        """
        pass

class Transaction(ABC):
    @abstractmethod
    def initiate(self, code: str, transaction_type: Account, recipient_account_number: str) -> bool:
        """
        Initiates a transaction with the provided code, transaction type, and recipient account number
        """
        pass

    @abstractmethod
    def validate(self, sender_account_number: str, recipient_account_number: str, transaction_amount: float) -> bool:
        """
        Validates the transaction with the given details
        """
        pass

    @abstractmethod
    def execute(self) -> bool:
        """
        Executes the transaction
        """
        pass

class Validator(ABC):
    @abstractmethod
    def has_enough_funds(self, sender_account_number: str, transaction_amount: float) -> bool:
        """
        Checks if the sender has enough funds to complete the transaction
        """
        pass

    @abstractmethod
    def check_transaction_limits(self, sender_account_number: str, transaction_amount: float) -> bool:
        """
        Checks if the transaction amount exceeds any limits
        """
        pass    

    @abstractmethod
    def ensure_transaction_security(self, code: str) -> bool:
        """
        Ensures the security of the transaction by verifying the provided code
        """
        pass        
