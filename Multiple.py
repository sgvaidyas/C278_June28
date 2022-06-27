class A:
    def disp(self):
        print("hi A class")

class B:
    def disp(self):
        print("hi B class")

class C(A,B):
    def disp(self):
        #A.disp(self)
        #B.disp(self)
        super().disp()


c = C()
c.disp()
