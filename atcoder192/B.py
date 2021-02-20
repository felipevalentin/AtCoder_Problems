s = input()
if len(s) == 1 and s.islower():
    print("Yes")
else:
    if s[::2].islower() and s[1::2].isupper():
        print("Yes")
    else:
        print("No")