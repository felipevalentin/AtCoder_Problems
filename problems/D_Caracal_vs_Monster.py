from math import log
h = int(input())
ans = 0
for i in range(int(log(h, 2))+1):
    ans += 2**(i)
print(ans)
