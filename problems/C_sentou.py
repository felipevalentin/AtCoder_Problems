N, T = map(int, input().split())
P = list(map(int, input().split()))
ans = T
for i in range(1, N):
    ans += min(T, P[i]-P[i-1])
print(ans)