S = input()
for i in range(7):
    if S[:7-i] + S[-i:] == "keyence":
        print("YES")
        break
else:
    print("NO")
