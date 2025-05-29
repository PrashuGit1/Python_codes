class A:
    def fun1(self):
        return ("This is fun1 from class A")


class B(A):
    def fun1(self):
        return (f"This fun1 from class B\n {super().fun1()}")
        


b=B()

print(b.fun1())

