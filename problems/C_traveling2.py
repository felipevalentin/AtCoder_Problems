t = x = y = 0
for i in range(int(input())):
    t1, x1, y1 = map(int, input().split())
    a, b = abs(x1-x)+abs(y1-y), t1-t
    t, x, y = t1, x1, y1
    if a > b or (a+b) % 2:
        print("No")
        break
else:
    print("Yes")
