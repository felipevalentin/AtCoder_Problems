S = input()
ans = a = 0
for s in S:
    if s == "B":
        a += 1
    else:
        ans += a
print(ans)

#A ideia é que contabilizamos quantos peças pretas estão na parta esquerda de cada
#peça branca e a partir dai sabemos quantas trocas serao possiveis 