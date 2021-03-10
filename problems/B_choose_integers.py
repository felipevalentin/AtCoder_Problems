from math import gcd
A, B, C = map(int, input().split())
print("NO" if C % gcd(A, B) else "YES")
