# Enter your code here. Read input from STDIN. Print output to STDOUT
var=input()
n, m=map(int, var.split())
k=0
def word():
    var='WELCOME'
    for v in var:
        yield v

class SymbolIterator:
    def __init__(self, pattern):
        self.pattern = pattern
        self.index = 0

    def __call__(self):
        char = self.pattern[self.index]
        self.index = (self.index + 1) % len(self.pattern)  # Loop back to start
        return char

it = SymbolIterator('.|.')

var=word()

for i in range(1,n+1):
    for j in range(1,m+1):

        #Above Line

        if(i < n//2+1):
            if(((m//2)-(3*i-3))<=j<=((m//2)+(3*i-1))):
                print(it(), end='')
            else:
                print('-', end='')

        #Middle line  

        elif(i==n//2+1):
            if(m//2-3<j<=m//2+4):
                print(next(var), end='')
            else:
                print('-', end='')
            k=i
        
        #Below line

        else:
            if((3*i-1)-(m//2)<=j<=(m-((i-k)*3))):
                print(it(), end='')
            else:
                print('-', end='')    
    print()