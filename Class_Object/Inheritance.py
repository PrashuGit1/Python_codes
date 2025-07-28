class A:
    def __init__(self):
        print("I am constractor from class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("I am constractor from class B")

ob1=B()
