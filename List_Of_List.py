def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # recursive flatten
        else:
            result.append(item)
    return result

lst = [5, 3, [8, 6], 4, [7], 2, 9, [[[[3, 7, 2.9]]]], [[9, 4, 6]]]
flat_list = flatten(lst)
print(flat_list)


