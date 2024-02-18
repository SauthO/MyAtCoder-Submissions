N, M, K = map( int, input().split() )

def gcd(N, M):
  n = min(N, M)
  m = max(N, M)
  if m%n==0:
    return n
  else:
    return gcd(n, m%n)

L = 0
R= 1*10**19
l = N*M/gcd(N,M) 

while (R-L)>=2:
  X = (L+R)//2
  if  X//N + X//M - 2*(X//l) >= K:
    R = X
  else:
    L = X
  
print(int(R))