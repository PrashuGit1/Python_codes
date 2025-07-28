n=int(input("Enter Number "))

for i in range(n//2+1):
    for j in range(n//2+1):
        if(j<=i):
            print('*', end='')
        else:
            print(' ', end='')
    
    for k in range(n//2):
        if(k>i):
            print(' ', end='')
        else:
            print('*', end='')


    
    print()


    
    