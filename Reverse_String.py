def reverse_str(str):
#method 1

    """str1=''
    for i in str[::-1]:
        str1=str1+i
    return str1"""


#Method 2
    return str[::-1]

#method 3

    #output will be in the list 
    """return list(reversed(str))"""

if __name__ == "__main__":
    str=input("Please Input the String \n")
    str1=reverse_str(str)
    print(str1)