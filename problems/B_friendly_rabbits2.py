N = int(input())
A = list(map(int, input().split()))
ans = sum(i == A[A[i]-1]-1 for i in range(N))
print(ans//2)
