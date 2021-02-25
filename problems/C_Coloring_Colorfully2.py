s = input()
ans = 0
for i, v in enumerate(s):
    if i % 2 ^ int(v):
        ans += 1
print(min(ans, len(s)-ans))
