a, b, c, x, y = map(int, input().split())
p = a*x + b*y
s = c*x*2 + b*max(0, y-x)
t = c*y*2 + a*max(0, x-y)
print(min(p, s, t))
