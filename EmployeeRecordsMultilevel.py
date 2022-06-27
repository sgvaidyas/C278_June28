class Company():
    def __init__(self):
        self.id = int(input("Enter company ID: "))
        self.name = input("Enter company name: ")

    def display(self):
        print("Company ID: ", self.id)
        print("Company name: ", self.name)


class Branch(Company):
    def __init__(self):
        super().__init__()
        self.branch_id = int(input("Enter branch ID: "))
        self.branch_name = input("Enter branch name: ")

    def display(self):
        super().display()
        print("Branch ID: ", self.branch_id)
        print("Branch name: ", self.branch_name)

class Employee(Branch):
    def __init__(self):
        super().__init__()
        self.emp_id = int(input("Enter employee ID: "))
        self.emp_name = input("Enter employee name: ")
        self.emp_salary = int(input("Enter employee salary: "))

    def display(self):
        super().display()
        print("Employee ID: ", self.emp_id)
        print("Employee name: ", self.emp_name)
        print("Employee salary: ", self.emp_salary)

employee_l = []
flag = True
while flag:
    print("1 Insert 2 Display All 3 Search for Employee record 4 Exit")
    ch = int(input("Enter the choice"))
    if ch ==1:
        employee1 = Employee()
        employee_l.append(employee1)
    elif ch==2:
        for employee in employee_l:
            employee.display()
    elif ch==3:
        name = input("Who are you searching for")
        isFound=False
        for emp in employee_l:
            if name == emp.emp_name:
                emp.display()
                isFound=True
        if isFound==False:
            print("We don't have that employee here, Get out")
    
