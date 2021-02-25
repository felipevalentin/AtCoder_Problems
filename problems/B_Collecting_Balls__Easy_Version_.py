n = int(input())
k = int(input())
x = list(map(int,input().split()))
t = 0
for i in x:
    if i <= k-i:
        t += i*2
    else:
        t += (k-i)*2
print(t)

