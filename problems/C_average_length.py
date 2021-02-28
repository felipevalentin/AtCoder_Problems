N = int(input())
c = []
for i in range(N):
    x, y = map(int, input().split())
    c.append([x, y])
d = 0
for i in range(N):
    for j in range(N):
        f = c[i]
        g = c[j]
        print(f, g)
        d += ((g[0]-f[0])**2 + (g[1]-f[1])**2)**(1/2)
print(d/N)
