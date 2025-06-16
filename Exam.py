def check_vowels(str):
    vowels=0
    consonants=0
    vowel='aeiou'
    for i in str.lower():
        if i.isalpha():
            if i in vowel:
                vowels+=1
            else:
                consonants+=1
    print(f"Vowels in this string is {vowels} \nConsonants in this string is {consonants}")







str='Prakash'
check_vowels(str)