H, W = map(int, input().split())
G = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if G[i][j] == "#" and "#" not in [G[max(i-1, 0)][j],
                                          G[min(i+1, H-1)][j],
                                          G[i][max(j-1, 0)],
                                          G[i][min(j+1, W-1)]]:
            print("No")
            exit()
print("Yes")
