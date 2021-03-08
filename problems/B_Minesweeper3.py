H, W = map(int, input().split())
S = [input() for _ in range(H)]
for i in range(H):
    ans = ""
    for j in range(W):
        if S[i][j] == "#":
            ans += "#"
        else:
            t = 0
            for x in range(-1, 2):
                if 0 <= i+x < H:
                    s = S[i+x]
                    t += (s[max([j-1, 0]):min([j+2, W])].count("#"))
            ans += str(t)
    print(ans)
