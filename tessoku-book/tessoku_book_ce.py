N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [0]*(Q+1)
R = [0]*(Q+1)

for q in range(1, Q+1, 1):
  L[q], R[q] = map(int, input().split())

part = [0]*(N+1)

for i in range(1, N+1, 1):
  part[i] = part[i-1] + A[i-1]


for q in range(1, Q+1, 1):
  if R[q]-L[q]+1 < 2*(part[R[q]]-part[L[q]-1]):
    print("win")
  elif R[q]-L[q]+1 == 2*(part[R[q]]-part[L[q]-1]):
    print("draw")
  else:
    print("lose")