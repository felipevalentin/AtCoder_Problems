input()
b = 0
for h in map(int, input().split()):
    b = max([b, h])
    if b - h > 1:
        print("No")
        break
else:
    print("Yes")
