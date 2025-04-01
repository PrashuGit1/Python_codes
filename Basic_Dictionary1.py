dic={'a': 1, 'd': 3, 'e':7, 'f':6, 'e':5, 'b': 2}
sorted_by_values = dict(sorted(dic.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_by_values)
