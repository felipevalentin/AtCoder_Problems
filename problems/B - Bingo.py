a = [input().split() for i in range(3)]
n = int(input())
b = [input() for i in range(n)]
ans = "No"
for i in a:
    if (i[0] in b) and (i[1] in b) and (i[2] in b):
        ans = "Yes"
for i in zip(*a):
    if (i[0] in b) and (i[1] in b) and (i[2] in b):
        ans = "Yes"
if a[0][0] in b and a[1][1] in b and a[2][2] in b:
    ans = "Yes"
if a[0][2] in b and a[1][1] in b and a[2][0] in b:
    ans = "Yes"
print(ans)
