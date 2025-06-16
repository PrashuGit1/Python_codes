def flatten_list(nested_list):
    result = []
    stack = nested_list[::-1]  # Start from the end for correct order

    while stack:
        current=stack.pop()
        if(isinstance(current, list)):
            stack.extend(current[::-1])
        else:
            result.append(current)
    return result
# Test the function
nested = [1, [2, 3], [4, [[[[[5, 6]]]]]], 7]
print(flatten_list(nested))  # Output: [1, 2, 3, 4, 5, 6, 7]
