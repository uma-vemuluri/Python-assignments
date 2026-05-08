from abc import ABC, abstractmethod

# Abstract Class
class UPIPayment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def check_balance(self):
       pass

class PhonePe(UPIPayment):

    def __init__(self):
        self.balance = 5000

    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Paid ₹{amount} using PhonePe")
        else:
            print("Insufficient balance in PhonePe")

    def check_balance(self):
        print(f"Remaining Balance in PhonePe: ₹{self.balance}")



class GooglePay(UPIPayment):

    def __init__(self):
        self.balance = 3000

    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Paid {amount} using GooglePay")
        else:
            print("Insufficient balance in GooglePay")

    def check_balance(self):
        print(f"Remaining Balance in GooglePay: ₹{self.balance}")


# Paytm Class
class Paytm(UPIPayment):

    def __init__(self):
        self.balance = 4000

    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Paid {amount} using Paytm")
        else:
            print("Insufficient balance in Paytm")

    def check_balance(self):
        print(f"Remaining Balance in Paytm: ₹{self.balance}")


# User Input
amount = int(input("Enter amount: "))

print("Choose Payment App")
print("1. PhonePe")
print("2. GooglePay")
print("3. Paytm")

choice = int(input("Enter your choice: "))


if choice == 1:
    obj = PhonePe()

elif choice == 2:
    obj = GooglePay()

elif choice == 3:
    obj = Paytm()

else:
    print("Invalid Choice")
    exit()

obj.pay(amount)
obj.check_balance()