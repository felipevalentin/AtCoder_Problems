n = int(input())
d, x = map(int, input().split())
for i in range(n):
    for i in range(1, d+1, int(input())):
        x += 1
print(x)