lst=[7, 12, 9, 11, 3]
for i in range(1, len(lst)):
    current_item=lst[i]
    index=i
    for j in range(i-1,-1,-1):
        if(lst[j]>current_item):
            lst[j+1]=lst[j]
            index=j
        else:
            break
    lst[index]=current_item

print(lst)