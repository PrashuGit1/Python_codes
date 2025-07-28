import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()               # Record start time
        result = func(*args, **kwargs)    # Run the original function
        end = time.time()                 # Record end time
        print(f"⏱ Function took {end - start:.2f} seconds to run.")
        return result                     # Return result as usual
    return wrapper

@timer
def slow_function():
    print("Sleeping for 2 seconds...")
    time.sleep(2)
    print("Done sleeping!")

slow_function()
