s = input()
p = 0
maior = 0
for i in s:
    if i in ("ACGT"):
        p += 1
    else:
        p = 0
    maior = max(maior, p)
print(maior)