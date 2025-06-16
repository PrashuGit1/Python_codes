t1=tuple(x**2 for x in range(1,6))

print(t1)



fruits = ("banana", "apple", "cherry")
if "apple" in fruits:
    print("Yes, 'apple' is in the tuple.")
else:
    print("No, 'apple' is not in the tuple.")



a, b, *c = (10, 20, 30, 40, 50)
print(a)  # 10
print(b)  # 20
print(c)  # [30, 40, 50]



print(tuple("abc")) #('a', 'b', 'c')



nested_list = [[1, 2], [3, 4]]
nested_tuple = tuple(tuple(x) for x in nested_list)
print(nested_tuple)


# Below code will gives dublicate

t = (1, 2, 3, 2, 4, 1)
duplicates = []

for i in t:
    if t.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)


students = [("John", 90), ("Sara", 85)]
for name, marks in students:
    print(f"{name}: {marks}")



location = {(12.5, 77.6): "Bangalore", (28.6, 77.2): "Delhi"}


