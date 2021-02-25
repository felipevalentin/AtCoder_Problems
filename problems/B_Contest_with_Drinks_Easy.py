n = int(input())
t = list(map(int, input().split()))
m = int(input())
for i in range(m):
    p, x = map(int, input().split())
    a = t[p-1]
    print(sum(t)-a+x)
