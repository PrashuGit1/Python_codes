str="my name is prakash shukla"
dic={}
lst=str.split()

for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)