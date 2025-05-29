def count_uppercase(s):
    x=0
    for i in s:
        if(i.isupper()):
            x+=1
    return x
if __name__ == "__main__":
    str="NxtWAve"
    print(count_uppercase(str))