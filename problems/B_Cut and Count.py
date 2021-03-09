N = int(input())
S = input()
ans = 0
for i in range(N):
    m = len(set(S[:i]) & set(S[i:]))
    ans = max(ans, m)
print(ans)
