n, b, r = map(int, input().split())
y, n = divmod(n, b + r)
ans = b * y + min(b, n)
print(ans)