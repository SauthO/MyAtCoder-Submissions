N = int(input())
X = [0]*(N+1)
Y = [0]*(N+1)
for n in range(1, N+1, 1):
  X[n], Y[n] = map(int, input().split())

Q = int(input())
a = [0]*Q
b = [0]*Q
c = [0]*Q
d = [0]*Q

for q in range(Q):
  a[q], b[q], c[q], d[q] = map(int, input().split())

# 点がある：１、点無い：０
Z = [ [0 for _ in range(1501)] for _ in range(1501)]
for n in range(1, N+1, 1):
  Z[Y[n]][X[n]] += 1

# 累積をとる
# 横方向
for y in range(1, 1501, 1):
  for x in range(1, 1501, 1):
    Z[y][x] += Z[y][x-1]
#縦方向
for x in range(1, 1501, 1):
  for y in range(1, 1501, 1):
    Z[y][x] += Z[y-1][x]

for q in range(Q):
  print(Z[d[q]][c[q]] - Z[d[q]][a[q]-1] - Z[b[q]-1][c[q]] + Z[b[q]-1][a[q]-1])
