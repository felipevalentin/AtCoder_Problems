n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
for i in range(n):
    ans += [sum(a[:i+1]) + sum(b[i:])]
print(max(ans))
