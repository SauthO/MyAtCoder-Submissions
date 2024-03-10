import bisect

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

L = int(input())
C = list(map(int, input().split()))

Q = int(input())
X = list(map(int, input().split()))

S = []

for n in range(N):
  for m in range(M):
    for l in range(L):
      S.append(A[n]+B[m]+C[l])

S.sort()
S = list(set(S))

def check(r, s, x):
  L = 0
  R = r
  if s[-1] < x:
    print("No")
    return
  
  while L<=R:
    M = (L+R)//2
    if s[M] < x:
      L = M+1
    elif s[M] > x:
      R = M-1
    else:
      print("Yes")
      break
    
    if L>R:
      print("No")

for q in range(Q):
  R = len(S)
  check(R, S, X[q])