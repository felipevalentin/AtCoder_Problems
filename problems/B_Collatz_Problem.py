a = [int(input())]
i = 2
while True:
    if a[i-2] % 2 == 0:
        a.append(a[i-2]/2)
    else:
        a.append(a[i-2]*3 + 1)
    if len(set(a)) < i:
        print(i)
        break
    i += 1