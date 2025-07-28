file=open('Example.txt', 'r')
content=file.read()
file.close()
vowels_count=0
vowels='aeiou'
for i in content.lower():
    if i in vowels:
        vowels_count+=1
print(vowels_count)
