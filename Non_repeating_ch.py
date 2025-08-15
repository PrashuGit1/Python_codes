def f_n_r_str(str):
    for i in str:
        if(str.count(i)==1):
            return i

if __name__ == "__main__":
    print(f_n_r_str("ppaddfhh"))


"""""def first_non_repeat_ch(txt):
    dic={}
    for i in txt:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    
    for i,j in dic.items():
        if(j==1):
            return ("First non repeating character is :", i)
            break
    



if __name__ == "__main__":
    txt = 'ppaddfhh'
    print(first_non_repeat_ch(txt))"""