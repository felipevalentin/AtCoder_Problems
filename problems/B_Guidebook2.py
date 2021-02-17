c = []
for i in range(int(input())):
    s, p = input().split()
    c.append([s, -int(p), i+1])
for i in sorted(c):
    print(i[2])
