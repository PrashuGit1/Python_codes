tu = ("apple", "banana", "cherry")
print(tu)
print(type(tu))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple_m = ("abc", 34, True, 40, "male")

print(tu[1])

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple Update 
thistuple1 = ("apple", "banana", "cherry")
y = list(thistuple1)
y.remove("apple")
thistuple1 = tuple(y)
print(thistuple1)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)