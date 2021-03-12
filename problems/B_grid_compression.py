H, W = map(int, input().split())
R = [False] * H
C = [False] * W
A = []
for i in range(H):
    t = input()
    A.append(t)
    if "#" in t:
        R[i] = True
        for j in range(W):
            if t[j] == "#":
                C[j] = True
for i in range(H):
    if R[i]:
        for j in range(W):
            if C[j]:
                print(A[i][j], end="")
        print()
