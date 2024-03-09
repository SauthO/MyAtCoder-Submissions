N, K = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = 10**9

def cum(t, A, n, K):
  S = 0
  for i in range(n):
    S += t//A[i]
  if K <= S:
    return True
  else:
    return False

while L<R:
  M = (L+R)//2
  if cum(M, A, N, K)==True:
    R = M
  else:
    L = M+1

print(L)