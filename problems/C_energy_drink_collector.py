N, M = map(int, input().split())
P = []
for i in range(N):
    A, B = map(int, input().split())
    P.append([A, B])
P.sort()
i = 0
ans = 0
while M > 0:
    x = P[i]
    if x[1] > M:
        ans += M * x[0]
        M = 0
    else:
        ans += x[0] * x[1]
        M -= x[1]
    i += 1
print(ans)
