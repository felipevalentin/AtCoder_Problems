a = int(input())
i = []
while a not in i:
    i.append(a)
    if a % 2 == 0:
        a /= 2
    else:
        a = a*3 + 1
print(len(i)+1)