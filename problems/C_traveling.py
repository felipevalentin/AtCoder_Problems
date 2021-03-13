N = int(input())
ans = "Yes"
t = x = y = 0
for i in range(N):
    t1, x1, y1 = map(int, input().split())
    if t1-t < (abs(x1-x) + abs(y1-y)):
        ans = "No"
    elif ((t1-t) % 2) != ((abs(x1-x) + abs(y1-y)) % 2):
        ans = "No"
    t, x, y = t1, x1, y1
print(ans)
