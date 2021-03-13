H, W = map(int, input().split())
G = [input() + "." for _ in range(H)] + ["."*W]
ans = "Yes"
for i in range(H):
    for j in range(W):
        if (G[i][j] == "#"
                and G[i-1][j] == G[i+1][j] == G[i][j-1] == G[i][j+1] == "."):
            ans = "No"
print(ans)
