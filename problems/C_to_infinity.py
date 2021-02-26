S = input()
K = int(input())
a = 1
for s in S:
    if s is not "1":
        print(s)
        break
    elif a == K:
        print(s)
        break
    a += 1
