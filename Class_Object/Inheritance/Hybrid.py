class A:
    def fun(self):
        print("Hello! I am fun from class A")
    
class B(A):
    def fun1(self):
        print("Hello! I am fun1 from class B")

class C:
    def fun2(self):
        print("Hello! I am fun2 from class C")

class D(B, C):
    def fun3(self):
        print("Hello ! I am fun3 from class D")
d = D()
d.fun()
d.fun1()
d.fun2()
d.fun3()
    