N = int(input())
X = [tuple(map(int, input().split())) for i in range(N)]
ans = sum(((c-a)**2 + (d-b)**2)**0.5 for a, b in X for c, d in X)
print(ans/N)
