s = input()
a = map(set, ["NS", "EW", "NSEW"])
if set(s) in a:
    print("Yes")
else:
    print("No")
