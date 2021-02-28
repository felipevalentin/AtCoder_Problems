N = int(input())
B = [input() for i in range(N)]
M = int(input())
R = [input() for i in range(M)]
ans = 0
for c in set(B):
    ans = max(ans, B.count(c) - R.count(c))
print(ans)
