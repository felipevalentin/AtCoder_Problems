x = input()
m = int(input())
d = int(max(x))
if len(x) == 1:
    print(+(int(x) <= m))
else:
    L, R = d, m+1
    while R-L > 1:
        M = (L+R) // 2
        a = 0
        for i in x:
            a *= M
            a += int(i)
            if a > m:
                R = M
                break
        else:
            L = M
    print(L - d)
