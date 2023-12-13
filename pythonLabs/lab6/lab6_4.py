s = input().split('.')
if len(s) != 4:
    print("NO")
else:
    for i in s:
        if not i.isdigit() or int(i) < 0 or int(i) > 255:
            print("NO")
            break
    else:
        print("YES")