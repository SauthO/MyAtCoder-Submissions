N = int(input())

P = list(map(int, input().split()))

Q = int(input())

A = [None] * Q
B = [None] * Q

for i in range(Q):
  A[i], B[i] = map(int, input().split())

for i in range(Q):
  if P.index(A[i]) > P.index(B[i]):
    print(B[i])
  else:
    print(A[i])