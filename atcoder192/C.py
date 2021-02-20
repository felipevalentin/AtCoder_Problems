n, k = input().split()
for i in range(int(k)):
    g1 = "".join(sorted(n, reverse=True))
    g2 = "".join(sorted(n))
    f = int(g1) - int(g2)
    n = str(f)
print(n)
