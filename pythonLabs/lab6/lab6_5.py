s = input().strip()
s = ' '.join(s.split())
s = s.replace(' ,', ',').replace(' .', '.')
print(s)