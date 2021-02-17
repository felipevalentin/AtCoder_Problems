s = input()
a = b = ""
ans = 0
for i in s:
    a += i
    if a != b:
        ans += 1
        a, b = "", a
print(ans)
