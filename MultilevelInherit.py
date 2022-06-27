class A:
    def __init__(self,a):
        print("Class A, a= ",a)

class B(A):
    def __init__(self,a,b):
        super().__init__(a) #A constructor(a) (11)
        print("Class B, b= ",b)

class C(B):
    def __init__(self,a,b,c):
        super().__init__(a,b) #Bconstructor(a,b) (11,22)
        print("Class C, c= ",c)

ob = C(11,22,33)
