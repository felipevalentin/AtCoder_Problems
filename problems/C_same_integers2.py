A, B, C = sorted(map(int, input().split()))
a, b = divmod(C-A + C-B, 2)
print(a + b*2)
