n = int(input())
m = [int(input()) for i in range(n)]
o = sorted(m)
for i in range(n):
    if m[i] != o[0]:
        print(o[-1])
    else:
        print(o[-2])
