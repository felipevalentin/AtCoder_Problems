n = int(input())
a = list(map(int, input().split()))
ans = 0
aux = 1
if 1 in a:
    for v in a:
        if v == aux:
            aux += 1
        else:
            ans += 1
    print(ans)
else:
    print(-1)
