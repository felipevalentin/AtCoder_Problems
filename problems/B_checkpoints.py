N, M = map(int, input().split())
S = [tuple(map(int, input().split())) for i in range(N)]
C = [tuple(map(int, input().split())) for i in range(M)]
for s in S:
    ans = [[abs(s[0] - c[0]) + abs(s[1] - c[1]), i+1] for i, c in enumerate(C)]
    print(min(ans)[1])
