x = int(input())
while any(x % i == 0 for i in range(2, int(x**(1/2)) + 1)):
    x += 1
print(x)
