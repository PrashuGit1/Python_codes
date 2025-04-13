def check_prime(n):
    k=0
    if(n==0 or n==1):
        print(n, "is not prime number")
    elif n>1:
        for i in range(2,n//2):
            if(n%i==0):
                k+=1
        if(k==0):
            print(n," is prime Number")
        else:
            print(n," is not prime Number")


if __name__== "__main__":
    n=int(input("Enter Number \n"))
    x=check_prime(n)
