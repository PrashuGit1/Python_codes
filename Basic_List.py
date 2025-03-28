#list can store any type of data

li=[1,2,3,1,3,1,4,5]
print(li)
print(li[0], li[-1])

li[2]=9
print(li)


# List Methods

li.append(13)
print(li)

l1=li.copy()
print(l1)

l1.clear()
print(l1)

print(li.count(1))

l2=[11,56,23]
li.extend(l2)
print(li)

print(li.index(3))

#insert method

li.insert(3, 10)
print(li)

li.pop()
print(li)

li.remove(3)
print(li)

li.reverse()
print(li)

li.sort()
print(li)

li.sort(reverse=True)
print(li)

print(li[1:7])
print(li[1:7:2])
print(li[-1:7:-1])

print(li[1:9])