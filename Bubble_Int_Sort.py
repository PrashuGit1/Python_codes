li=[12,13,11,15,17,18,6,3,7,9]
for i in range(len(li)-1):
    for j in range(len(li)-i-1):
        if(li[j]>li[j+1]):
            tmp=li[j]
            li[j]=li[j+1]
            li[j+1]=tmp
            
print(li)