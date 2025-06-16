def my_decorator(func):
    print('before the wrapper')
    def wrappr():
        print("something is happing before the function is called")
        func()
        print("Something is happing after the function is called")
    return wrappr
    print('after the wrappr')

@my_decorator
def say_hello():
    print("Hello ! I am old function")

say_hello()