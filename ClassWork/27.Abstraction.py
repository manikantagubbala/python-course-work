#27.Abstraction.py
# Hide the data, ABC - Abstract Base Class

from abc import ABC,abstractmethod

class BankAccount(ABC):
    def deposit(self):
        print("You can deposit your amount.")

    @abstractmethod
    def withdraw(self):
        pass

    def viewhistory(self):
        print("You can see all the Transactions.")


class savingAccount(BankAccount):
    def withdraw(self):
        print("You can withdraw your amount.")

account = savingAccount()
account.deposit()
account.withdraw()
account.viewhistory()