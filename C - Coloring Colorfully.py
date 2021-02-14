s = input()
ans = 0
for i, v in enumerate(s):
    if i % 2:
        if v == "1":
            ans += 1
    else:
        if v == "0":
            ans += 1
print(min(ans, len(s)-ans))
