def outer_function(x):
    def inner_function(y):
        return x + y  # inner function uses x from outer function
    return inner_function

add_five = outer_function(5)  # x = 5
print(add_five(10))           # y = 10 => Output: 15
