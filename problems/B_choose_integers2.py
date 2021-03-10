from math import gcd
A, B, C = map(int, input().split())
T = any(A*i % B == C for i in range(1, B+1))
print("YES" if T else "NO")

# a lógica está que se não há nenhum A * i para todo i menor que B igual a C
# então nunca haverá, pois os valores do módulo dos multiplos de A vão se
# repetir a cada intervalo de B,
