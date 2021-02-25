a, b = map(int, input().split())
x = max(a//0.08 + 1, b//0.1 + 1)
y = min((a+1)//0.08, (b+1)//0.1)
if x < y:
    print(int(x))
else:
    print(-1)
