s = input()
ans = pos = 1
ant = s[0]
while pos < len(s):
    if s[pos] == ant:
        ans += 1
        pos += 2
        ant = ""
        if pos > len(s):
            ans -= 1
    else:
        ant = s[pos]
        ans += 1
        pos += 1
print(ans)
