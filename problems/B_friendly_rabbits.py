N = int(input())
A = input().split()
ans = set()
for i in range(N):
    a = sorted([i, int(A[i])-1])
    ans.add(tuple(a))
print(N - len(ans))
