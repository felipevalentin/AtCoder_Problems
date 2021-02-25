n, m = map(int, input().split())
f = []
ans = 0
for i in range(n):
    f += input().split()[1:]
for i in range(1, m+1):
    if f.count(str(i)) == n:
        ans += 1
print(ans)
