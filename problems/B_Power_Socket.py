a, b = map(int, input().split())
disp = 1
ans = 0
while disp < b:
    disp += a-1
    ans += 1
print(ans)