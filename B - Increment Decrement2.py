n = int(input())
s = input()
H = X = 0
for i in s:
    X += 1 if i == "I" else -1
    H = max(H, X)
print(H)
