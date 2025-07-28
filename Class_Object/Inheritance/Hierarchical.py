class parent:
    def show(self):
        print("parent class")
    
class child1(parent):
     def show(self):
        print("Child1 class")

class child2(parent):
     def show(self):
        print("Child2 class")

ch1 = child1()
ch1.show()

ch2 = child2()
ch2.show()