words = ["apple", "bat", "banana", "car", "ant"]
grouped = {}

for word in words:
    first_letter = word[0]
    grouped.setdefault(first_letter, []).append(word)

print(grouped)
# {'a': ['apple', 'ant'], 'b': ['bat', 'banana'], 'c': ['car']}