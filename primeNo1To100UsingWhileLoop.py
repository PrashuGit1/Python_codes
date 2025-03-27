n=0
while(n<100):
    n=n+1
    c=0
    i=2
    while(i<n):
        if(n%i==0):
            c=c+1
            break
        i=i+1
    if(c==0):
        print(n,"prime No")
    else:
        print(n,"Not prime no")
