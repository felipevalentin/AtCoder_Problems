n, d = map(int, input().split())
x = []
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    x.append(a)
for i in range(n):
    for j in range(i+1, n):
        t = 0
        for a, b in zip(x[i], x[j]):
            t += (a-b)**2
        t = t**(1/2)
        if t.is_integer():
            ans += 1
print(ans)
