n = int(input())
a = {}
for i in range(n):
    s = input()
    a[s] = a.get(s, 0) + 1
h = max(a.values())
for v in sorted(a):
    if a[v] == h:
        print(v)
