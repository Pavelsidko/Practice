s = input()
unique_chars = []
for char in s:
    if s.count(char) == 1:
        unique_chars.append(char)
if len(unique_chars) == 0:
    print("NO")
else:
    unique_chars.sort()
    print("".join(unique_chars))