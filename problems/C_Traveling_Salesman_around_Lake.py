k, n = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
d = []
for i in range(1, n):
    a = l[i] - l[i-1]
    if a > k/2:
        a = (l[i-1]+k) - l[i]
    d.append(a)
a = l[-1] - l[0]
if a > k/2:
    a = (l[0]+k) - l[-1]
d.append(a)
d.remove(max(d))
print(sum(d))