n = int(input())
t, a = map(int, input().split())
h = [abs(t-int(x)*0.006-a) for x in input().split()]
print(h.index(min(h))+1)
