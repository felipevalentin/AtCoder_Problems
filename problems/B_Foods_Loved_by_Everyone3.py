n, m = map(int, input().split())
ans = set.intersection(*[set(input().split())[1:] for i in range(m)])
print(len(ans))
