class Company:
  def __init__(self):
    self.Id = 0
    self.Name = ""
    self.Loc = ""
    self.No_of_branches = 0

  def setdata(self):
    self.Id = int(input("Set an Id: "))
    self.Name = input("Set an Name: ")
    self.Loc = input("Set an Location: ")
    self.No_of_branches = int(input("Set the number of branches: "))

class Amazon(Company):
  def __init__(self):
    self.No_of_Departments = 0
    self.No_of_projects = 0
  def setdata(self):
    super().setdata()
    self.No_of_Departments = int(input("Set the number of departments: "))
    self.No_of_projects = int(input("Set the number of projects: "))

  def __str__(self):
      s = "No of Dept = " + str(self.No_of_Departments)
      s = s+ "\nNo of Projects = " +str(self.No_of_projects)
      return s

class Yahoo(Company):
  def __init__(self):
    self.No_of_Departments = 0
    self.No_of_Employees = 0
  def setdata(self):
    super().setdata()
    self.No_of_Departments = int(input("Set the number of departments: "))
    self.No_of_Employees = int(input("Set the number of employees: "))

ob = Amazon()
ob.setdata()
print(ob)
