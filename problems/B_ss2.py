S = input()[:-2]
while S[:len(S)//2] != S[len(S)//2:]:
    S = S[:-2]
print(len(S))
