N, S, K = map(int, input().split())
P = [None]*N
Q = [None]*N

for i in range(N):
  P[i], Q[i] = map(int, input().split())
  
sum = 0

for i in range(N):
  sum += P[i]*Q[i]

if sum < S:
  sum += K
  
print(sum)  