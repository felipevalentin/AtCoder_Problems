s = input()
for i in range(ord("a"), ord("z")+1):
    if chr(i) not in s:
        print(chr(i))
        break
else:
    print("None")
