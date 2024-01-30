N = int(input())
A = [0] + list(map(int, input().split()))
D = int(input())
L = [0]*(D+2)
R = [0]*(D+2)

for i in range(1, D+1, 1):
  L[i], R[i] = map(int, input().split())

P = [0]*(N+2)
Q = [0]*(N+2)

for i in range(1, N+1, 1):
  P[i] = max(A[i], P[i-1])
  Q[N+1-i] = max(A[N+1-i], Q[N+1-i+1])

for i in range(1, D+1, 1):
  print(max(P[L[i]-1], Q[R[i]+1]))