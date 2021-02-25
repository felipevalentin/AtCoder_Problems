input()
ans = 0
for i in input().split():
    a = int(i)
    while a % 2 == 0:
        ans += 1
        a /= 2
print(ans)
