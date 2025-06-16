person = {}

# CREATE
person["name"] = "Prakash"
person.update({"age": 25, "city": "Delhi"})

# READ
print(person["name"])
print(person.get("country", "Not Found"))

# UPDATE
person["age"] = 26
person.setdefault("gender", "Male")

# DELETE
person.pop("city")
del person["gender"]
person.clear()


x = ('key1', 'key2', 'key3')
new_dict = dict.fromkeys(x, [])
new_dict['key1'].append(1)
print(new_dict)

