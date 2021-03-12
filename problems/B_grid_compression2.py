H, W = map(int, input().split())
R = []
for i in range(H):
    t = input()
    if "#" in t:
        R.append(t)
C = []
for i in zip(*R):
    if "#" in i:
        C.append(i)
for i in zip(*C):
    print("".join(i))
