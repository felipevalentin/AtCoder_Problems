s = input()
ans = min(abs(753 - int(s[i:i+3])) for i in range(len(s)-2))
print(ans)