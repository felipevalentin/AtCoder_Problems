X = int(input())
ans = [i**n for i in range(33) for n in range(2, 10) if i**n <= X]
print(max(ans))
