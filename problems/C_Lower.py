n = int(input())
h = list(map(int, input().split()))
ans = maior = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        maior += 1
    else:
        maior = 0
    ans = max(ans, maior)
print(ans)
