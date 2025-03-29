Days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thourday', 'Friday', 'Saturday']

Days.sort()

for i in range(len(Days)-1):
    for j in range(len(Days)-1):
        if(len(Days[j])>len(Days[j+1])):
            tmp=Days[j]
            Days[j]=Days[j+1]
            Days[j+1]=tmp

print(Days)

            
