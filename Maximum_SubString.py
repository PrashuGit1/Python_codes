#There is two condition
# First character should not repeat and second return the maximum lenght of the subscring 

def test_1(string =""): 
      
    # initializing the substring 
    substring = ""  
    testList = [] 
    initial = 0
      
    for char in string: 
          
        for i in range(initial, len(string)): 
            substring+= string[i] 
              
              
            # checking conditions 
            if substring.count(string[i])>1: 
                testList.append(substring[:-1]) 
                initial+= 1
                substring = "" 
                break
    maxi ="" 
      
    for word in testList: 
          
        if len(word)>len(maxi): 
            maxi = word 
              
    if len(maxi)<3: 
        return "-1"
    else: 
        return maxi 
      
# Driver code 
print(test_1("character"))


"""def mx_string(txt):
    mx=''
    store=''
    for i in range(0, len(txt)):
        for j in range(i, len(txt)):
            if txt[j] not in store:
                store+=txt[j]
            else:
                if(len(store)>len(mx)):
                    mx=store
                    store=''
                    break
                else:
                    store=''
                    break
                
                
    return mx

print(mx_string('character'))"""