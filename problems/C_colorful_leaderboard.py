N = int(input())
A = list(map(int, input().split()))
ans = set()
aux = 0
for a in A:
    if a < 3200:
        ans.add(a//400)
    else:
        aux += 1
x = len(ans)
print(x if x > 0 else 1, x+aux)
