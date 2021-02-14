import itertools
x = list(itertools.permutations(range(1, int(input())+1)))
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
print(abs(x.index(p) - x.index(q)))
