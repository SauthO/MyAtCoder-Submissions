n, X = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
for i in range(n):
  if int(X/2**i)%2 == 1:
    sum += a[i]
  
print(sum)