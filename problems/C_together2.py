input()
ans = dict()
for a in map(int, input().split()):
    for i in (-1, 0, 1):
        ans[a+i] = ans.get(a+i, 0) + 1
print(max(ans.values()))
