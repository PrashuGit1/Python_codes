def longest_string(str):
    lst=str.split()
    """mx=0
    for i in lst:
        if(mx<len(i)):
            mx=len(i)
            str1=i
    return str1"""
    
    return max(lst, key=len)

if __name__ == "__main__":
    print(longest_string("The fox jumps over the lazy dog"))