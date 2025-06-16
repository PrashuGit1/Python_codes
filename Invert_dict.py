d = {'a': 1, 'b': 2, 'c': 1}
inverse = {}
for keys, values in d.items():
    inverse.setdefault(values, []).append(keys)

print(inverse)