from collections import Counter

def count_each_vowel(s):
    s = s.lower()
    vowel_count = Counter(ch for ch in s if ch in 'aeiou')
    print(vowel_count)
    print(type(vowel_count))

count_each_vowel('Prakash')
  


