N = int(input())
X = [tuple(map(int, input().split())) for i in range(N)]
ans = 0
for a, b in X:
    for c, d in X:
        ans += ((c-a)**2 + (d-b)**2)**0.5
print(ans/N)
