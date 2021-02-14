n = int(input())
x = list(map(int, input().split()))
p = round(sum(x)/n)
print((sum((i-p)**2 for i in x)))