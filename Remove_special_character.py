def remove_special_characters(text):
    result = ''
    for char in text:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9'):
        #if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57:
        # Keep character

            result += char
    return result

text = 'Pra@ka#sh.1'
print(remove_special_characters(text))  # Output: Prakash1
