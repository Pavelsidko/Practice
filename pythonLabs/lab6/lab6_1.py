def Capitalize(S):
    return ' '.join(word.capitalize() for word in S.split())


s = str(input())
result = Capitalize(s)
print(result)