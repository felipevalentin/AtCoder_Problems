a, b = map(int, input().split())
if a*b <= 0:
    print("Zero")
else:
    if a < 0:
        n = b - a + 1
        if n % 2 == 0:
            print("Positive")
        else:
            print("Negative")
    else:
        print("Positive")
