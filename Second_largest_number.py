def getSecondLargest(arr):
    """mx=max(arr)
    while mx in arr:
        arr.remove(mx)
    return (max(arr))"""


    """n=len(arr)
    for i in range(n-1):
        for j in range(n-1):
            if(arr[j]<arr[j+1]):
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
    for x in range(n):
        if(arr[x]!=arr[0]):
            return arr[x]"""


    mx=-100
    smx=-100
    n=len(arr)
    for i in range(n):
        if(mx<arr[i]):
            smx=mx
            mx=arr[i]
        elif(smx<arr[i] and arr[i]!=mx):
            smx=arr[i]
    return smx

        
    

if __name__ == "__main__":
    arr = [-100,-1,-99]
    print(getSecondLargest(arr))
