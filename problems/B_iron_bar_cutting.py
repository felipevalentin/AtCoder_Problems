N = int(input())
A = list(map(int, input().split()))
ans = set()
L, R = 0, len(A)-1
while L <= R:
    M = (L+R)//2
    ans.add(abs(sum(A[:M])-sum(A[M:])))
    if sum(A[:M]) == sum(A[M:]):
        ans.add(0)
        break
    elif sum(A[:M]) < sum(A[M:]):
        L = M+1
    else:
        R = M-1
print(min(ans))
