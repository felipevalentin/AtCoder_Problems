N = int(input())
A = dict()
for i in range(N):
    t = int(input())
    A[t] = A.get(t, -1) * -1
print(sum(a > 0 for a in A.values()))
