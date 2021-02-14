n, m = map(int, input().split())
s = ""
for i in range(m):
    s += input()
for i in range(1, n+1):
    print(s.count(str(i)))
