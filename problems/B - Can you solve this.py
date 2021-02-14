n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    t = c
    d = list(map(int, input().split()))
    for i in range(m):
        t += b[i] * d[i]
    if t > 0:
        ans += 1
print(ans)