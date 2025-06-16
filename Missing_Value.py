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


"""def fun(*lst):
    lst1=[]
    last=lst[-1]
    for i in range(0,last):
        if i not in lst:
           lst1.append(i)
           i+=1
    print(lst1)

fun(1,2,5,6,8,9)"""


"""def fun(*args):
    lst1=[]
    last=args[-1]//2
    for i in range(1,last):
        if(i*2) not in args:
            lst1.append(i*2)
            i+=2
    print(lst1)

fun(2,4,8,10,14)"""
