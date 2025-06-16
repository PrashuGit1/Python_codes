def dublicate_val(lst):
    dic={}
    for i in lst:
       if i in dic:
        dic[i]+=1
       else:
          dic[i]=1
    for i in lst:
        print(f"{i} is frequency is: ", dic[i])


if __name__ == "__main__":
    lst = [1, 2, 3, 2, 4, 5, 1]
    value=dublicate_val(lst)


"""lst = [1, 2, 2, 3, 1, 1]
dic={}
for i in lst:
    dic[i]=dic.get(i,0)+1
print(dic)"""