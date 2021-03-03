N = int(input())
A = list(map(int, input().split()))
ans = 3**N
aux = 1
for a in A:
    if a % 2 == 0:
        aux *= 2
print(ans-aux)
