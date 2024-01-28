N = int(input())
a = list(map(int, input().split()))

dp = [1e8]*N
dp[0] = 0
dp[1] = abs(a[0]-a[1])

for i in range(2, N, 1):
  one_step = dp[i-1]+abs(a[i]-a[i-1])
  two_step = dp[i-2]+abs(a[i]-a[i-2])
  dp[i]=min(one_step, two_step)
  
print(dp[N-1])