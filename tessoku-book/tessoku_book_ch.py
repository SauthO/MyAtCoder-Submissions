N = int(input())
A = [0]*N
B = [0]*N
C = [0]*N
D = [0]*N

for n in range(N):
  A[n], B[n], C[n], D[n] = map(int, input().split())

X = [ [0 for _ in range (1501)] for _ in range(1501) ]

for n in range(N):
  X[A[n]][B[n]] += 1
  X[A[n]][D[n]] -= 1
  X[C[n]][B[n]] -= 1
  X[C[n]][D[n]] += 1

#横方向 累積和 
for i in range(1501):
  for j in range(1, 1501, 1):
    X[i][j] = X[i][j-1] + X[i][j]

#縦方向 累積和
for j in range(1501):
  for i in range(1, 1501, 1):
    X[i][j] = X[i-1][j] + X[i][j]

cnt = 0
for i in range(1501):
  for j in range(1501):
    if X[i][j]!=0:
      cnt += 1
print(cnt)