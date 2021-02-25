h, w = map(int, input().split())
c = [input() for i in range(h)]
for i in range(2*h):
    th = i//2
    for j in range(w):
        print(c[th][j], end="")
    print()
