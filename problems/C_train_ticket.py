from itertools import product
A, B, C, D = input()
E = product("+-", "+-", "+-")
for e in E:
    t = A+e[0]+B+e[1]+C+e[2]+D
    if eval(t) == 7:
        print(t+"=7")
        break
