x = int(input())
while True:
    for i in range(2, int(x**(1/2))):
        if x % i == 0:
            break
    else:
        print(x)
        break
    x += 1