input()
ans = 0
for i in map(int, input().split()):
    ans += bin(i)[::-1].index("1")
print(ans)
# Converte a resposta o número em binário, pois a posição do primeiro 1, indica
# o número de vezes que aquele número é divisível por 2. por exemplo 1111, não é 
# divisível, pois o número se encontra na primeira casa, mas 1100 é divisível 
# 2 vezes pois o primeiro 1 se encontra na terceira casa,