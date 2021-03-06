S = input()
ans = 0
aux = 0
for i, s in enumerate(S[::-1]):
    if s == "B":
        ans += i-aux
        aux += 1
print(ans)
