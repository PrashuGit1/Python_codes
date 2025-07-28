def compress_repeating_character(txt):
    if not txt:
        return ""

    result = ""
    count = 1

    for i in range(1, len(txt)):
        if txt[i] == txt[i - 1]:
            count += 1
        else:
            result += txt[i - 1] + str(count)
            count = 1  # reset count

    result += txt[-1] + str(count)  # handle last group
    return result

# Test case
txt = 'aaabcccdd'
print(compress_repeating_character(txt))  # a3b1c3d2


"""def com_rep_ch(text):
    txt=''
    j=''
    count=1
    for i in text:
        if(j==''):
            j=i
        elif(i==j):
            count+=1
        elif(i!=j):
            txt+=j+str(count)
            count=1
            j=i
    txt+=j+str(count)
    return txt



text='aajjjkaaggh'
print(com_rep_ch(text))"""