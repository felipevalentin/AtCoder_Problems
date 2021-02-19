n, x = map(int, input().split())
w = []
ans = ""
for i in range(n):
    w.append(input())
for i in range(n):
    ans += min(w)
    w.remove(min(w))
print(ans)
