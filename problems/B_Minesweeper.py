H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = [[0]*(W+2) for _ in range(H+2)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            for y in range(-1, 2):
                for x in range(-1, 2):
                    ans[i+y][j+x] += 1
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            print("#", end="")
        else:
            print(ans[i][j], end="")
    print()
