n, m = map(int, input().split())
ac = [0]*n
wa = [0]*n
w = 0
for i in range(m):
    p, s = input().split()
    p = int(p)-1
    if ac[p] == 0 and s == "AC":
        ac[p] = 1
        w += wa[p]
    wa[p] += 1
print(sum(ac), w)
