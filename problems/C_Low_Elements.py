n = input()
p = list(map(int, input().split()))
ans = 0
m = p[0]
for i in p:
    if i <= m:
        m = i
        ans += 1
print(ans)
