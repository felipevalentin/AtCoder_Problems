n = int(input())
a = list(map(int, input().split()))
b = sorted(range(1, n+1), key = lambda num: a.__getitem__(num-1))
print(*b)