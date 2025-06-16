def freq_count(str):
    dic={}
    
    for i in str:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1

    print(dic)



str='prakasss'
freq_count(str)