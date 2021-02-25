s = input()
for i in s:
    if s.count(i) % 2 == 1:
        print("No")
        break
else:
    print("Yes")
