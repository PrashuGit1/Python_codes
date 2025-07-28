lst=[2,5,4,9,2,4]
var=8
dic={}


for i, j in enumerate(lst):
    n=var-j
    if n in dic:
        print(i,dic[n])
        break
    dic[j]=i