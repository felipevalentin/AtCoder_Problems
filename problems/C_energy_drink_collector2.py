N, M = map(int, input().split())
P = (tuple(map(int, input().split())) for i in range(N))
ans = 0
for a, b in sorted(P):
    t = min(M, b)
    ans += a*t
    M -= t
print(ans)
