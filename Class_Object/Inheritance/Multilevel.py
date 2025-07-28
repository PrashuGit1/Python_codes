class Grandparent:
    def old_skill(self):
        print("Farming")

class Parent(Grandparent):
    def new_skill(self):
        print("Business")

class Child(Parent):
    def my_skill(self):
        print("Programming")

c = Child()
c.old_skill()
c.new_skill()
c.my_skill()
