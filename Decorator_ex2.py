def custom_message(txt):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(txt)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@custom_message("🚨 Accessing secure zone!")
def secure_function():
    print("Sensitive work happening...")

secure_function()
