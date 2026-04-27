#Task : 
'''Encapsulation Task 1: E-Commerce Product
Instructions:
Create a class Product
Create private variable for price
Add method set_price(price)
Accept only values greater than 0
Add method apply_discount(percent)
Discount should not exceed 50%
Update price after discount
Add method get_price()
Return current price'''
class Product:
    def __init__(self):
        self.__price = 0   # private variable

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price! Must be greater than 0.")

    def apply_discount(self, percent):
        if 0 < percent <= 50:
            discount_amount = (percent / 100) * self.__price
            self.__price -= discount_amount
        else:
            print("Invalid discount! Cannot exceed 50%.")

    def get_price(self):
        return self.__price
o = Product()
o.set_price(1000)
o.apply_discount(20)
print("Current price after discount:", o.get_price())



'''Encapsulation Task 2: Mobile Lock System
📌 Instructions:
Create a class Mobile
Create private variable for password
Add method set_password(pwd)
Password must be at least 4 characters
Add method unlock(pwd)
Check password and print result
Add method change_password(old_pwd, new_pwd)
Change only if old password is correct
New password must follow rules'''

class Mobile:
    def __init__(self):
        self.__password = None   # private variable

    def set_password(self, pwd):
        if len(pwd) >= 4:
            self.__password = pwd
            print("Password set successfully.")
        else:
            print("Password must be at least 4 characters.")

    def unlock(self, pwd):
        if self.__password == pwd:
            print("Mobile unlocked.")
        else:
            print("Incorrect password.")

    def change_password(self, old_pwd, new_pwd):
        if self.__password == old_pwd:
            if len(new_pwd) >= 4:
                self.__password = new_pwd
                print("Password changed successfully.")
            else:
                print("New password must be at least 4 characters.")
        else:
            print("Old password is incorrect.")
o = Mobile()
o.set_password("1234")
o.unlock("1234")
o.change_password("1234", "5678")
o.unlock("5678")
# o/p:
# Password set successfully.
# Mobile unlocked.
# Password changed successfully.
# Mobile unlocked.

'''
✅ Encapsulation Task 3: HR Employee System
📌 Instructions:
Create a class Employee
Create private variables:
__salary
__designation
Add method set_salary(salary)
Salary should be greater than 0
Prevent invalid updates
Add method get_salary()
Return salary
Add method set_designation(role)
Allow only specific roles (e.g., "Manager", "Developer", "HR")
Add method get_designation()
Return designation
Add method increment_salary(percent)
Increase salary based on percentage
Percentage should not exceed 30%
Do not allow direct access to salary or designation from outside the class'''

class Employee:
    def __init__(self):
        self.__salary = 0
        self.__designation = None

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary! Must be greater than 0.")

    def get_salary(self):
        return self.__salary

    def set_designation(self, role):
        allowed_roles = ["Manager", "Developer", "HR"]
        if role in allowed_roles:
            self.__designation = role
        else:
            print("Invalid designation!")

    def get_designation(self):
        return self.__designation

    def increment_salary(self, percent):
        if 0 < percent <= 30:
            increment = (percent / 100) * self.__salary
            self.__salary += increment
        else:
            print("Increment cannot exceed 30%.")
o = Employee()
o.set_salary(50000)
o.set_designation("Developer") 
print("Current Salary:", o.get_salary())
print("Current Designation:", o.get_designation())
o.increment_salary(20)
print("Salary after increment:", o.get_salary())

#o/p:
#Current Salary: 50000
#Current Designation: Developer
#Salary after increment: 60000.0