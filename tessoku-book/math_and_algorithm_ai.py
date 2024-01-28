N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [0]*Q
R = [0]*Q

for i in range(Q):
  L[i], R[i] = map(int, input().split())


part = [0]*N
part[0] = A[0]
for n in range(1, N, 1):
  part[n] += A[n] + part[n-1]
for q in range(Q):
  if L[q]!=1:
    print(part[R[q]-1]-part[L[q]-2])
  else:
    print(part[R[q]-1])
    
