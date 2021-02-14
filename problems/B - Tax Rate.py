a = int(input())
x = int(a//1.08) + 1
if int(x*1.08) == a:
    print(x)
else:
    print(":(")