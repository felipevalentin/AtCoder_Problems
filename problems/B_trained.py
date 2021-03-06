N = int(input())
A = []
for i in range(N):
    A.append(int(input())-1)

ans = 0
act = 0
while ans <= N and act != 1:
    act = A[act]
    ans += 1
print(-1 if ans > N else ans)
