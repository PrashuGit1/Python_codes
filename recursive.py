"""def reverse_recursion(str):
    if len(str)==0:
        return str
    else:
        return reverse_recursion(str[1:]) + str[0]

str='prakash'
print(reverse_recursion(str))"""


def reverse_recursion(str):
    if len(str)==0:
        return str
    else:
        return str[len(str)-1] + reverse_recursion(str[:len(str)-1])

str='prakash'
print(reverse_recursion(str))
    