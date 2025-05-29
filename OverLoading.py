class calculator:
    def add(self, a, b=0,c=0):
        return a+b+c

a=calculator()
print(a.add(10))
print(a.add(10, 20))
print(a.add(10, 20, 30))