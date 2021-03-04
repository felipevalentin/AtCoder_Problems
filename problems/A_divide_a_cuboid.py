A, B, C = sorted(map(int, input().split()))
c = C // 2
print(A*B*(C-c) - A*B*c)
