v = [100, 101, 102, 103, 104, 105]
x = int(input())
for i in v:
    if x % i in v + [0] or x > 2100:
        print(1)
        break
else:
    print(0)
