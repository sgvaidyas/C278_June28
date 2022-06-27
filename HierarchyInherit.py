class Person:
    def __init__(self):
        self.name = ""
        self.id = 0

    def setdata(self):
        self.name = input("Enter the name = ")
        self.id = int(input("Enter the id = "))

    def display(self):
        print("NAME   =  ",self.name)
        print("ID     =  ",self.id)

class Student(Person):
    def setdata(self):
        super().setdata()
        self.courseId = int(input("Enter Course Id"))

    def display(self):
        super().display()
        print("Course ID  =  ",self.courseId)


class Staff(Person):
    def setdata(self):
        super().setdata()
        self.sem = int(input("Enter Semister"))
        self.courses = eval(input("Enter the list of courses handled"))

    def display(self):
        super().display()
        print("SEM   =  ",self.sem)
        print("Courses handled  = ",self.courses)

stu = Student()
stu.setdata()
stu.display()

staf = Staff()
staf.setdata()
staf.display()
