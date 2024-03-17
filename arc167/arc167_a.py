N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

B = [0]*M

cnt = N

for m in range(2*M):
  if m<M:
    B[m] += A[m]
  else:
    B[-(m-M+1)] += A[m]
  cnt -= 1
  if cnt ==0 :
    break

B_sq = 0
for i in range(M):
  B_sq += B[i]**2
print(B_sq)