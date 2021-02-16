s = input()
ans = "Yes"
if "N" in s and "S" not in s:
    ans = "No"
elif "W" in s and "E" not in s:
    ans = "No"
elif "S" in s and "N" not in s:
    ans = "No"
elif "E" in s and "W" not in s:
    ans = "No"
print(ans)
