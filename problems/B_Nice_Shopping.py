x = lambda: map(int, input().split())
a, b, m = x()
al = list(x())
bl = list(x())
menor = min(al) + min(bl)
for i in range(m):
    ax, bx, c, = x()
    menor = min(menor, al[ax-1] + bl[bx-1] - c)
print(menor)