N = int(input())
S = sorted([int(input()) for _ in range(N)])
a = sum(S)
if a % 10:
    print(a)
else:
    for s in S:
        if s % 10:
            print(a-s)
            break
    else:
        print(0)
