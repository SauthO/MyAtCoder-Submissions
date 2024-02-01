N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x, N, K, A):# cntがK以上の時にフラグをたてる
  cnt = 0
  for i in range(N):
    cnt += x//A[i]
  
  if cnt >= K:
    return True
    
  return False

l = 1
r = 10**9

while l<r:
  
  m = (l+r)//2
  ans = check(m, N, K, A)
  if ans == False:
    l = m + 1
  
  if ans == True:
    r = m

print(l)
    