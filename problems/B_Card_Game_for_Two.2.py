input()
l = sorted(map(int, input().split()), reverse=True)
print(sum(l[::2]) - sum(l[1::2]))