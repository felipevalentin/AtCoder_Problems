S = input()
K = "keyence"
for i in range(len(K)):
    if S[:len(K)-i] in K and S[len(S)-i:] in K:
        print("YES")
        break
else:
    print("NO")
