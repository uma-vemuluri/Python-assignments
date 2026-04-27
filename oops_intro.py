'''Task 1: Student System 
👉 Question: Create a class Student 
with: Class variable: school_name = "XYZ School" A method set_details() → inside method, assign: name = "Vamsi" marks = 85 A method display() → print: Name Marks School name 
👉 Outside the class: Create object Call set_details() Call display()'''
class student:
  school_name = "XYZ School" #cls variable
  def set_details(self):
    self.name = "Uma"
    self.marks = 85
  def display(self):
    print(self.name)
    print(self.marks)
    print(self.school_name)

o = student()
o.set_details()
o.display()
#O/p: Uma
#85
#XYZ School

'''👉 Question:
Create a class Employee with:
Class variable: company = "Infosys"
A method set_data()
 → assign:
name = "Ravi"
salary = 20000
A method increase_salary()
 → add 5000 to salary
A method display()
 → print all details
👉 Outside the class:
Create object
Call all methods
***italicized text***'''
class Employee:
  company = "Infosys"
  def set_data(self):
     self.name = "Ravi"
     self.salary = 20000
  def increase_salary(self):
    self.salary += 5000
  def display(self):
    print( self.name)
    print(self.salary)
    print(self.company)
o = Employee()
o.set_data()
o.increase_salary()
o.display()
#O/p: Ravi
#25000
#Infosys
'''👉 Question: Create a class Mobile with: 
Class variable: brand = "Apple" A method set_details() 
→ assign: model = "iPhone 14" price = 80000 A method discount()
 → reduce price by 10% A method show_details() 
→ print all details 
👉 Outside the class: Create object Call methods'''
class mobile:
  brand = "Apple"
  def set_details(self):
    self.model = "iPhone 14"
    self.price = 80000
  def discount(self):
    self.price *= 0.9
  def show_details(self):
    print(self.brand)
    print(self.model)
    print(self.price)
o = mobile()
o.set_details()
o.discount()
o.show_details()
#O/p: Apple
#iPhone 14 
#72000.0
