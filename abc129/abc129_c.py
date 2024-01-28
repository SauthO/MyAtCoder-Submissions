N, M = map(int, input().split())
a = list(int(input()) for _ in range(M))

num = 1000000007

dp = [1]*(N+1)
for a_i in a:
  dp[a_i]=0

for i in range(2, N+1, 1):
  if(dp[i]!=0):
    dp[i] = dp[i-2]+dp[i-1]

print(dp[N]%num)