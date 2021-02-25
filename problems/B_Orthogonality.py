x = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = 0
for i, j in zip(a, b):
    t += i*j
print("Yes" if t == 0 else "No")
