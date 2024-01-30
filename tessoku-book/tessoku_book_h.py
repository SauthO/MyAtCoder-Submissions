H, W = map(int, input().split())
X = [0]*H
for h in range(H):
  X[h] = list(map(int, input().split()))

Q = int(input())
A = [0]*Q
B = [0]*Q
C = [0]*Q
D = [0]*Q

for q in range(Q):
  A[q], B[q], C[q], D[q] = map(int, input().split())

#累積
Z = [ [0 for _ in range(W+1)] for _ in range(H+1) ]

#幅方向
for h in range(H):
  for w in range(W):
    Z[h+1][w+1] = Z[h+1][w] + X[h][w]

#縦方向
for w in range(W):
  for h in range(H):
    Z[h+1][w+1] += Z[h][w+1]
  
for q in range(Q):
  print(Z[C[q]][D[q]] - Z[C[q]][B[q]-1] - Z[A[q]-1][D[q]] + Z[A[q]-1][B[q]-1])