n = input()
a = len(n)
print(max([sum(int(i) for i in n), int(n[0])-1 + (a-1)*9]))
