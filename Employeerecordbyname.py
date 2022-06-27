class Company:
    def __init__(self):
        self.id = 1
        self.name = "JPMC"

class Branch(Company):
    def __init__(self):
        super().__init__()
        self.branchID = 1
        self.branchName = "Houston "
        self.employees = []

    def addEmployee(self):
        ob = Employee()
        self.employees.append(ob)

    def showEmployees(self):
        for emp in self.employees:
            emp.display()

    def showByName(self):
        name = input("Who are you searching for")
        isFound=False
        for emp in self.employees:
            if name == emp.empName.split()[0]:
                emp.display()
                isFound=True
        if isFound==False:
            print("We don't have that employee here, Get out")

class Employee(Branch):
    def __init__(self):
        self.empName = input("What is your full name")
        self.empID = int(input("What's your ID"))
        self.empSalary = int(input("What's your annual salary *no commas*"))

    def display(self):
        print(f"My name is {self.empName} and I make ${self.empSalary} per year")

branch = Branch()
branch.addEmployee()
branch.addEmployee()
branch.showEmployees()
branch.showByName()
