S = sorted([int(input()) for _ in range(int(input()))])
a = sum(S)
for s in S:
    if a % 10:
        break
    elif s % 10:
        a -= s
print(a if a % 10 else 0)
