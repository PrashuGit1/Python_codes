def right_rotation(lst, k):
    k = k % len(lst)  # handle cases where k > len(lst)
    return lst[-k:] + lst[:-k]

lst = [1, 2, 3, 4, 5]
k = 2
print(right_rotation(lst, k))  # Output: [4, 5, 1, 2, 3]
