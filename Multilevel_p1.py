class Year:
    def __init__(self):
        self.currentYear = int(input("Enter year"))
        self.noOfStudent = int(input("Enter no of students"))

class Course(Year):
    def __init__(self):
        super().__init__()
        self.CourseId = int(input("Enter course Id"))
        self.CourseName = input("Enter course Name")

class Student(Course):
    def __init__(self):
        super().__init__()
        self.name = input("Enter the name = ")
        self.roll = int(input("Enter the roll = "))
        self.marks = []

    def setmarks(self):
        n = int(input("Enter the no of subjects = "))
        for i in range(n):
            m = int(input("Enter marks = "+ str(i) +" = "))
            self.marks.append(m)
        self.total = sum(self.marks)
        self.avg = self.total/n

    def display(self):
        print("Total    =  ",self.total)
        print("Average  =  ",self.avg)


s = Student()
s.setmarks()
s.display()
