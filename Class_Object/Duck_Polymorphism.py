class Dog:
    def speak(self):
        print("Bark!")

class Cat:
    def speak(self):
        print("Meow!")

class Human:
    def speak(self):
        print("Hello!")

def call_speak(animal):
    animal.speak()

# All of them have a speak() method
call_speak(Dog())     # Bark!
call_speak(Cat())     # Meow!
call_speak(Human())   # Hello!
