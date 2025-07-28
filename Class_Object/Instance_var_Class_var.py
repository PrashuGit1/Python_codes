class Student:
    School_name='Prakash school'
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f"name: {self.name}, Marks: {self.marks}, School: {self.School_name}")

d1=Student('Prakash', 88)
d2=Student("Ravi", 92)
d1.display_info()
d2.display_info()

#updating School name for both
Student.School_name='xyz School'
d1.display_info()
d2.display_info()

d1.School_name='abc School'
d1.display_info()
d2.display_info()
