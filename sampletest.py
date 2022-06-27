class Sample:
    def __init__(self):
        self.fname = input("Enter fname = ")
        self.lname = input("Enter lname = ")

    @property
    def fullname(self):
        return self.fname + " " + self.lname
    @property
    def email(self):
        return self.fname + "_" + self.lname+"@wiley.com"

ob = Sample()
print(ob.fullname)
print(ob.email)

