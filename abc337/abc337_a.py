N = int(input())
X = [0]*N
Y = [0]*N
for n in range(N):
  X[n], Y[n] = map(int, input().split())
  
sum_x = 0
sum_y = 0

for n in range(N):
  sum_x += X[n]
  sum_y += Y[n]

if sum_x > sum_y:
  print("Takahashi")
elif sum_x < sum_y:
  print("Aoki")
else:
  print("Draw")