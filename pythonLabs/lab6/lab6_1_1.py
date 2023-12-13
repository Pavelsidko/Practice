def Сapitalize(s):
    result = ""
    new_word = True
    for char in s:
        if new_word and char.isalpha():
            result += char.upper()
            new_word = False
        else:
            result += char.lower()
            if not char.isalpha():
                new_word = True
    return result

s = str(input())
result = Сapitalize(s)
print(result)
