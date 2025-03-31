def find_missing(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i

    min = lst[0]
    for i in lst:
        if i < min:
            min = i

    list1 = []

    for num in range(min + 1, max):
        if num not in lst:
            list1.append(num)

    return list1


# Driver code
lst = [5, 6, 10, 11, 13]
print(find_missing(lst))