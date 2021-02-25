a, b = input().split()
x = int(a+b)
if x**(1/2) % 1:
    print("No")
else:
    print("Yes")