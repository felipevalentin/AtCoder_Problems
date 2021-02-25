n, a, b = map(int, input().split())
c = b-a
if c % 2 == 0:
    print(c//2)
else:
    print(min(a, n-b+1) + c//2)
