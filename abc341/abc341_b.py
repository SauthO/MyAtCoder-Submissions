N = int(input())
A = list(map(int, input().split()))
S = [None]*N
T = [None]*N

for i in range(1, N, 1):
  S[i], T[i] = map(int, input().split())

for i in range(1, N, 1):
  if S[i] <= A[i-1]:
    A[i] += int(A[i-1]/S[i]) * T[i]

print(A[N-1])