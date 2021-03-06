S = input()[:-2]
while True:
    x = len(S)//2
    if S[:x] == S[x:]:
        print(len(S))
        break
    else:
        S = S[:-2]
