class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):  # overrides parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

for pet in [Dog(), Cat()]:
    pet.sound()  # same method name, different output
