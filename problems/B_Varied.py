s = input()
v = []
for i in s:
    if i in v:
        print("no")
        break
    v.append(i)
else:
    print("yes")
