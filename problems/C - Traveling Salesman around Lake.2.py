k, n = map(int, input().split())
l = list(map(int, input().split()))
l.append(l[0]+k)
a = max(l[i+1]-l[i] for i in range(n))
print(k-a)