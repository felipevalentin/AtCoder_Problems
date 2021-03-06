N = int(input())
A = [int(input())-1 for i in range(N)]
ans = a = 0
while ans < N and a != 1:
    a = A[a]
    ans += 1
print(ans if ans < N else -1)
