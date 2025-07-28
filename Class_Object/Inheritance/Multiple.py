class Father:
    def quality1(self):
        print("Hardworking")

class Mother:
    def quality2(self):
        print("Caring")

class Child(Father, Mother):
    def my_quality(self):
        print("I am awesome")

c = Child()
c.quality1()
c.quality2()
