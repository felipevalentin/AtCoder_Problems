N = int(input())
A = list(map(int, input().split()))
b = ans = sum(A)
for a in A:
    b -= a*2
    ans = min(ans, abs(b))
print(ans)
