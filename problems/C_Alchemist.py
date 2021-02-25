input()
v = list(map(int, input().split()))
v.sort()
s = v[0]
for i in v:
    s = (s+i) / 2
print(s)