''' SINGLE INHERITANCE TASK 🎯 Scenario: Online Course Platform
 👉 Parent Class: Course course_name price method → show_course() 
 👉 Child Class: ProgrammingCourse language duration method 
→ show_programming_course()'''
# class course:
#   course_name = "Data Science"
#   price = 35000
#   def show_course(self):
#     print(self.course_name)
#     print(self.price)

# class ProgrammingCourse(course):
#   lanuage = "python"
#   duration = "2 months"
#   def show_programming_course(self):
#     print(self.lanuage)
#     super().show_course()
#     print(self.duration)
# o=ProgrammingCourse()
# #o.show_course()
# o.show_programming_course()
# #O/p: python
# #Data Science   
# #35000
# #2 months

''' 2 MULTIPLE INHERITANCE TASK
 Scenario: Smart Phone Features
👉 Parent 1: Camera
camera_mp
method → take_photo()
👉 Parent 2: MusicPlayer
brand
method → play_music()
👉 Child: SmartPhone
model_name
method → show_details()

🧑‍💻 Task:
Create 2 smartphones
Call both parent methods
Print all features
👉 Goal:'''
class Camera:
    camera = "12MP"
    def take_photo(self):
        print("photo taken with",self.camera,"camera")
class MusicPlayer:
    brand = "sony"
    def play_music(self):
        print("playing music on",self.brand,"music player")
class SmartPhone(Camera, MusicPlayer):
    model_name = "samsung galaxy"
    def show_details(self):
        print("model name:",self.model_name)
        print(super().brand)
o = SmartPhone()
o.take_photo()
o.play_music()
o.show_details()
#O/p: photo taken with 12MP camera
#playing music on sony music player
#model name: samsung galaxy
#sony


''' MULTILEVEL INHERITANCE TASK
 Scenario: Education System
👉 Class 1: School  school_name
method → show_school() 👉 Class 2: Teacher (inherits School)
teacher_name
subject
method → show_teacher() 👉 Class 3: Student (inherits Teacher)  student_name
grade
method → show_student()

🧑‍💻 Task:
Create 2 students
Use super() in all classes
Print full hierarchy details
👉 Goal:
 Understand chain inheritance'''

class School:
    school_name = "Z.p High School"
    def show_school(self):
        print("my school name is",self.school_name)
class Teacher(School):
    teacher_name = "Apparao"
    subject = "Physics"
    def show_teacher(self):
        print("my teacher name is:",self.teacher_name )
class Student(Teacher):
    stud_name ="Uma"
    grade = "A+"
    def show_student(self):
        print("my name is:",self.stud_name)
        print("my grade is:",self.grade)
        super().show_school()
        super().show_teacher()
        print("subject:",self.subject)
o = Student()
o.show_student()


 ''' HIERARCHICAL INHERITANCE TASK
 Scenario: Food Delivery App
 Parent: User
name
location
method → login()
👉 Child 1: Customer  order_item method → place_order()
👉 Child 2: DeliveryPartner  vehicle_type
method → deliver_order() 🧑‍💻 Task:
Create 1 customer and 1 delivery partner
Use super()
Show login + role-specific actions
👉 Goal:
 Same base class → different behaviors'''

class user:
    name ="uma"
    loc = "hyderabad"
    def login(self):
        print(self.name,"logged in from",self.loc)
class customer(user):
    order_item ="pizza"
    def place_order(self):
        print("order placed",self.order_item)
        super().login()
class DeliveryPartner(user):
    vechile_type ="bike"
    def deliver_order():
        print("delivering order using",self.vechile_type)
        print(f"to {super().loc}")
o = customer()
o.place_order()
d = DeliveryPartner()
d.deliver_order()
 #o/p:
#order placed pizza
#uma logged in from hyderabad
#delivering order using bike
#to hyderabad

