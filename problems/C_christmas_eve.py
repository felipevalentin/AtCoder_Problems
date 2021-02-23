n, k = map(int, input().split())
t = []
for i in range(n):
    t.append(int(input()))
t.sort()
ans = t[-1] - t[0]
for i in range(n-k+1):
    ans = min(ans, t[k-1+i] - t[i])
print(ans)