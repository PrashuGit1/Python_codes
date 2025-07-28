def my_decorator(func):
    def wrapper(a, b):
        print("Hello wrapper !")
        if(isinstance(a, int) and isinstance(b, int)):
            result=func(a, b)
            return (f"Result : {result}")
        else:
            return ("invalid Input") 
    return wrapper



def add(a, b):
    return a+b

add=my_decorator(add)
print(add(5,10))