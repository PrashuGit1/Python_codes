class parent:
    def add(self, a,b):
        return a+b
class child(parent):
    def add(self, a,b,c):
        return a+b+c
    
obb=child()
print(obb.add(1,2,5))