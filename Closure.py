def fun1(a):
    def fun2(b):
        return a+b
    return fun2

var=fun1(10)
print(var(5))