n, m = map(int, input().split())
ac = [0]*n
wa = [0]*n
for i in range(m):
    p, s = input().split()
    p = int(p)-1
    if ac[p] == 0:
        if s == "AC":
            ac[p] = 1
        else:
            wa[p] += 1
print(sum(ac), sum([wa[x]*ac[x] for x in range(n)]))
