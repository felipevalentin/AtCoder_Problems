a, b, k = map(int, input().split())
ans = range(a, b+1)
ans = set(ans[:k]) | set(ans[-k:])
print(*sorted(ans), sep="\n")
