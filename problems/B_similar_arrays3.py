N = int(input())
A = input().split()
b = sum(int(a) % 2 == 0 for a in A)
print(3**N - 2**b)
