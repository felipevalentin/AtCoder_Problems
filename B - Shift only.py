input()
a = list(map(int, input().split()))
ans = a[0]
for i in a:
    temp = 0
    while i % 2 == 0:
        i /= 2
        temp += 1
    ans = min(temp, ans)
print(ans)