n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += min(a[i]+a[i+1], b[i])
    a[i+1] -= min(max(b[i]-a[i], 0), a[i+1])
print(ans)
