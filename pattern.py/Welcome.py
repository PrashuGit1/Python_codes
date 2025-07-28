row, col = map(int, input().split())

mid=row//2+1

sym='.|.'
word='WELCOME'

for i in range(1, row+1):
    if(i==mid):
        print(word.center(col,'-'))
        
    if(i<mid):
        print(((2*i-1)*sym).center(col,'-'))
    
    if(i>mid):
        print(((2*(row-i)+1)*sym).center(col,'-'))