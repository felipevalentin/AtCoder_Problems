a = [input().split() for i in range(3)]
n = int(input())
b = [input() for i in range(n)]
a += [i for i in zip(*a)]
a += [[a[i][i] for i in range(n)]]
a += [[a[i][2-i] for i in range(n)]]
for i in a:
    if all(j in b for j in i):
        print("Yes")
        break
else:
    print("No")
