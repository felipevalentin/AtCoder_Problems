n = int(input())
i = int(n**(1/2))
while n % i:
    i -= 1
j = n//2
print(i+j-2)
