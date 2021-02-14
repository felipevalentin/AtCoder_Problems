a, b, c = map(int, input().split())
x = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    if a == b == c:
        x = -1
        break
    a, b, c = (b+c) / 2, (a+c) / 2, (a+b) / 2
    x += 1
print(x)
