def even_number(a,b):
    for i in range(a,b):
        if i%2==0:
            yield i

gen=even_number(2,12)
print(type(gen))
for i in gen:
    print(i)