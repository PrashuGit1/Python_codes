class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_person(cls, name):
        return cls(name)  # 👈 No hardcoding — uses class dynamically

class Student(Person):
    pass

s = Student.create_person("Alice")
print(type(s))  # ✅ Gives <class '__main__.Student'>
