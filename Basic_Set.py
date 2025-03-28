#Set items are unchangeable, but you can remove items and add new items


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set_m = {"abc", 34, True, 40, "male"}

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" not in thisset)

#Once a set is created, you cannot change its items, but you can add new items.

thisset1 = {"apple", "banana", "cherry"}
thisset1.add("orange")
print(thisset1)


