input()
ans = [0]*100002
for a in map(int, input().split()):
    for i in (0, 1, 2):
        ans[a+i] += 1
print(max(ans))
