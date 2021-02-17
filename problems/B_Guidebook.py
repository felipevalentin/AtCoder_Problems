c = []
for i in range(int(input())):
    s, p = input().split()
    c.append([i+1, s, int(p)])
for i in sorted(c, key=lambda x: (x[1], -x[2])):
    print(i[0])
