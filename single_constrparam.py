class A:
    def __init__(self,a,b):
        self.val1 = a
        self.val2 = b

    def display(self):
        print("Val1 ",self.val1)
        print("Val2 ",self.val2)

class B(A):
    def __init__(self,a,b):
        super().__init__(a,b)
        print("CLASS B")

ob = B(44,66)
ob.display()
