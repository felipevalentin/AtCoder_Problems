n = int(input())
c = list(map(int, input().split()))
a, b = [], []
for i in range(n):
    x = max(c)
    if i % 2 == 0:
        a.append(x)
    else:
        b.append(x)
    c.remove(x)
print(sum(a) - sum(b))
