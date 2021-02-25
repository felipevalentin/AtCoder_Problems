n = int(input())
H = list(map(int, input().split()))
m = H[0]
for h in range(1, n):
    if m - H[h] > 1:
        print("No")
        break
    m = max(m, H[h])
else:
    print("Yes")
