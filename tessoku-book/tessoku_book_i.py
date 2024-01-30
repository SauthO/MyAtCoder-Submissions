H, W, N = map(int, input().split())
A = [0]*(N+1)
B = [0]*(N+1)
C = [0]*(N+1)
D = [0]*(N+1)

for n in range(1, N+1, 1):
  A[n], B[n], C[n], D[n] = map(int, input().split())

Z = [[0 for _ in range(W+2)] for _ in range(H+2)]

#flagをたてる　横方向のみ
for n in range(1, N+1, 1):
  for i in range(A[n], C[n]+1, 1):
    Z[i][B[n]] += 1
    Z[i][D[n]+1] -= 1

#横方向に累積
for h in range(1, H+1, 1):
  for w in range(1, W+1, 1):
    Z[h][w] += Z[h][w-1]


for h in range(1, H+1, 1):
  for w in range(1, W+1,1):
    if(w>1):
      print(" ", Z[h][w], end="")
    else:
      print(Z[h][w], end="")
  if h!=H:
    print("")