N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [1e10] * (N)
dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2, N, 1):
  if(i<K):
    for j in range(i):
      dp[i] = min(dp[i], dp[j]+abs(h[i]-h[j]))
  else:
    for j in range(K):
      dp[i] = min(dp[i], dp[i-K+j]+abs(h[i]-h[i-K+j]))
  
print(dp[N-1])