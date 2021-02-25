n = int(input())
a = list(map(int, input().split()))
b = 0
for i in a:
    if i == b+1:
        b += 1
print(n-b if b else -1)
