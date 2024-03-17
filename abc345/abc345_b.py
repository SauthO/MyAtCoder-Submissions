import math
X = int(input())

sho = X//10
amari = X%10

if amari != 0:
  print(sho+1)
else:
  print(sho)