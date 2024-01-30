N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [0]*Q
for q in range(Q):
  X[q] = int(input())
  
A.sort()
A = [1e-10]+A+[1e10]

for q in range(Q):
  R = N
  L = 1
  M = (R+L)//2
  discovered = False
  while not discovered:
    if A[M]<X[q] and X[q]<=A[M+1]:
      discovered = True
      print(M)
    elif X[q]<=A[M]:
      R = M-1
    else:
      L = M+1
    M = (R+L)//2