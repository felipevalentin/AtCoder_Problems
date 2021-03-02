A, B, C, D = input()

for i in "+-":
    for j in "+-":
        for k in "+-":
            t = A+i+B+j+C+k+D
            if eval(t) == 7:
                print(t+"=7")
                exit()
