k, n = map(int, input().split())
print(min(k % n, -k % n))