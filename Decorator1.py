def my_decorator(func):
    def wrapper(a, b):
        if(isinstance(a, int) and isinstance(b, int)):
            result=func(a, b)
            return (f"Result : {result}")
        else:
            return ("invalid Input") 
    return wrapper


@my_decorator
def add(a, b):
    return a+b


print(add(5,10))