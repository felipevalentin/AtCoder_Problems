n = input()
A = map(int, input().split())
a = set()
b = 0
for i in A:
    if i < 3200:
        a.add(i//400)
    else:
        b += 1
c = len(a)
print(max(c, 1), b+c)
