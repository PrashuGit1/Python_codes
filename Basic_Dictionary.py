thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

thisdict1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict1["colors"])

#x = thisdict.keys()
#print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change


thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.update({"year": 2020})
print(thisdict2)


# remove Item by pop

thisdict.pop("model")
print(thisdict)

# last Item has deleted using popitem()

thisdict.popitem()
print(thisdict)

del thisdict2["model"]
print(thisdict2)

"""del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists"""


print("\nAccessing the dictionaries \n")

dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for z in dict1:
    print(z)

print("\nprinting the Value\n")

for k in dict1:
    print(dict1[k])

