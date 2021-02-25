n, k, q = map(int, input().split())
j = [k-q] * n
for i in range(q):
    a = int(input())
    j[a-1] += 1
for i in j:
    if i > 0:
        print("Yes")
    else:
        print("No")
