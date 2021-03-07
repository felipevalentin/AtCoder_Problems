S = input()
ans = [0]*(len(S)+1)
for i, s in enumerate(S):
    if s == "<":
        ans[i+1] += ans[i] + 1
for i in range(len(S)-1, -1, -1):
    if S[i] == ">" and ans[i] <= ans[i+1]:
        ans[i] = ans[i+1] + 1
print(sum(ans))
