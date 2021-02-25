n = int(input())
r = n**(1/2)
if r.is_integer():
    print(int((r-1)*2))
else:
    a = int(r)
    b = int(n / a)
    while a*b != n:
        a -= 1
        b = int(n / a)
    print(int(a-1 + b-1))
