class student:
    def __init__(self,name, roll_no, marks):
        self.Name=name
        self.Roll_no=roll_no
        self.Marks=marks

    def display(self):
        print(f"Name: {self.Name}, Roll_no: {self.Roll_no}, Marks: {self.Marks}")

    def get_grade(self):
        if(self.Marks>90):
            print(f"Name: {self.Name}, Grade: A")
        elif(self.Marks>75):
            print(f"Name: {self.Name}, Grade: B")
        else:
            print(f"Name: {self.Name}, Grade: c")


p1=student('Prakash',101,87)
p1.get_grade()

