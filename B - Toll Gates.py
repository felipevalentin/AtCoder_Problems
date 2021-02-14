n, m, x = map(int, input().split())
a = list(map(int, input().split()))
s = sum(i < x for i in a)
print(min(s, m-s))