N = int(input())
ans = dict()
for a in map(int, input().split()):
    ans[a-1] = ans.get(a-1, 0) + 1
    ans[a] = ans.get(a, 0) + 1
    ans[a+1] = ans.get(a+1, 0) + 1
print(max(ans.values()))
