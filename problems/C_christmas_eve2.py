n, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])
print(min([t[k+i-1] - t[i] for i in range(n-k+1)]))
