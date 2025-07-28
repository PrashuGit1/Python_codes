def use_yeild(n):
    for i in range(n):
        yield i

for i in use_yeild(3):
    print(i)