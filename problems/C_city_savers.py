n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.reverse()
b.reverse()
ans = 0
for i in range(n):
    ans += min(a[i], b[i])
    b[i] -= a[i]
    if b[i] > 0:
        ans += min(a[i+1], b[i])
        a[i+1] = max(0, a[i+1]-b[i])
print(ans)
