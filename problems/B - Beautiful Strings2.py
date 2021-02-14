s = input()
ans = any(s.count(x) % 2 for x in s)
print("No" if ans else "Yes")
