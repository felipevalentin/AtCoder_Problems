n, m = map(int, input().split())
ans = set(range(m+1))
for i in range(n):
    k, *a = map(int, input().split())
    ans &= set(a)
print(len(ans))
