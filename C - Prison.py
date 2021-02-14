x = lambda: map(int, input().split())
n, m = x()
L, R = 0, n
for i in range(m):
    l, r = x()
    L = max(l, L)
    R = min(r, R)
print(max(0, R - L + 1))
