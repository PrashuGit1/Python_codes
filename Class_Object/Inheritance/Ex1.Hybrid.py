class A:
    def __init__(self):
        print("A constructor")

class B:
    def __init__(self):
        print("B constructor")

class C(A, B):   # Hybrid
    def __init__(self):
        B.__init__(self)   # Manually calling B
        A.__init__(self)   # Manually calling A
        print("C constructor")

obj = C()





