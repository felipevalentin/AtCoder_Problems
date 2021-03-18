R, G, B, N = map(int, input().split())
ans = 0
for i in range(3001):
    for j in range(3001):
        if (N - R*i - G*j) >= 0 and (N - R*i - G*j) % B == 0:
            ans += 1
print(ans)

# problema de otimizacao entregue em pypy