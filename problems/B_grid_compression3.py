H, W = map(int, input().split())
R = [r for r in [input() for i in range(H)] if "#" in r]
C = [c for c in zip(*R) if "#" in c]
for r in zip(*C):
    print("".join(r))
