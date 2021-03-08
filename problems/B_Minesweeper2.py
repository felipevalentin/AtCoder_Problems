H, W = map(int, input().split())
S = [input() for _ in range(H)]
for i in range(H):
    ans = ""
    for j in range(W):
        if S[i][j] == "#":
            ans += "#"
        else:
            t = 0
            for s in S[max([0, i-1]):min([i+2, H])]:
                t += (s[max([j-1, 0]):min([j+2, W])].count("#"))
            ans += str(t)
    print(ans)
