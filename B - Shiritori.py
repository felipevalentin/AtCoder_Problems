w = []
ans = "Yes"
for i in range(int(input())):
    s = input()
    if not w:
        w.append(s)
    else:
        if s not in w and s[0] == w[-1][-1]:
            w.append(s)
        else:
            ans = "No"
print(ans)
