N, Y = map(int, input().split())
flg = 0

for x in range(N+1):
  for y in range(N+1-x):
    z = N - x - y
    if(10000*x + 5000*y + 1000*z == Y):
      print(x, " ", y, " ", z)
      flg = 1
      break
    
  if(flg ==1):
    break

if flg==0:
  print(-1, " ", -1, " ", -1)