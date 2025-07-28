class A:
    def __init__(self):
        print("Constructor of A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of B")

class C:
    def __init__(self):
        print("Constructor of C")

class D(B, C):  # Hybrid Inheritance: D inherits from B (A) and C
    def __init__(self):
        super().__init__()
        print("Constructor of D")

obj = D()

