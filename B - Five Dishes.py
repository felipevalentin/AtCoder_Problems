t = a = 0
for i in range(5):
    x = int(input())
    q, r = divmod(-x, 10)
    t += -q * 10
    if r > 0:
        a = min(a, -r)
print(t+a)
