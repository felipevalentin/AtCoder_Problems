a, b = map(int, input().split())
s = input()
if a+b+1 == len(s) and s[a] == "-" and s.replace("-", "", 1).isdigit():
    print("Yes")
else:
    print("No")
