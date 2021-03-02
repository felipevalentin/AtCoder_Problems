A, B, C = sorted(map(int, input().split()))
ans = C-A + C-B
if ans % 2:
    print(ans//2 + 2)
else:
    print(ans//2)
