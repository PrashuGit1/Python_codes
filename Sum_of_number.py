def Sum_of_number(n):
    k=0
    while(n>=0):
        k=k+n
        n=n-1
    return k


if __name__=="__main__":
    n=int(input("Enter the number"))
    s=Sum_of_number(n)
    print(s)