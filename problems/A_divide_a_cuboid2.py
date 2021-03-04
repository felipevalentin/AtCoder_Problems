A, B, C = sorted(map(int, input().split()))
print(A*B * (A*B*C % 2))
