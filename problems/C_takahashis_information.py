C = [list(map(int, input().split())) for i in range(3)]
b1 = C[0][0]
b2 = C[0][1]
b3 = C[0][2]
a1 = 0
a2 = C[1][0] - b1
a3 = C[2][0] - b1
D = []
for i in [a1, a2, a3]:
    line = []
    for j in [b1, b2, b3]:
        line.append(i+j)
    D.append(line)
if C == D:
    print("Yes")
else:
    print("No")
