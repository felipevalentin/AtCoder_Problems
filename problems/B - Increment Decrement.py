n = input()
s = input()
H = X = 0
for i in s:
    if i == "I":
        X += 1
    else:
        X -= 1
    H = max(H, X)
print(H)
