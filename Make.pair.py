lst=[4,4,4,4,8,8,8,6,7,7]
lst1=[]
count={}
for num in lst:
    count[num]=count.get(num, 0)+1
    if(count[num]==2):
        lst1.append((num, num))
        count[num]=0
print(lst1)