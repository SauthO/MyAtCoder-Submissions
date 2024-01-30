N, X= map(int, input().split())
A = list(map(int, input().split()))

discovered = False
R = len(A)-1
L = 0
M = (R+L)//2

while not discovered:
  if X<A[M]:
    R = M-1
  elif X==A[M]:
    print(M+1)
    discovered = True
  else:
    L = M+1
  M = (R+L)//2
    