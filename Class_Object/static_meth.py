class MyClass:
    @staticmethod
    def greet(name):  # ✅ Clear: this is not tied to instance or class
        print(f"Hello, {name}!")

# MyClass.greet("Prakash")  # ✅ Works perfectly
obj=MyClass()
obj.greet("prakash")




