import random

total = 275
a=random.randint(1, total-2)
b=random.randint(1,total-1-a)
c=total-a-b
print(a,b,c)
print('total:', a+b+c)