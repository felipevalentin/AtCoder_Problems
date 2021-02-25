input()
a = 0
for h in map(int, input().split()):
    if h < a:
        print("No")
        break
    h -= a < h
    a = h
else:
    print("Yes")
# Se o anterior - 1 é maior que o atual, não é possível
# Isso se da ao fato que se a altura atual é maior que a proxima, então reduzimos 
# 1 da proxima altura, pois estamos levando adiante a menor altura possivel
# portanto se a posição atual for menor que a menor altura possiver, então 
# é impossível alinhar em ordem nao descrescente
