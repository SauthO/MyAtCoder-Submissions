N = int(input())
h = list(map(int, input().split()))

dp = [0]*N
dp[0] = 0
dp[1] = abs(h[0]-h[1])

for i in range(2, N, 1):
    two_step = dp[i-2]+abs(h[i-2]-h[i])
    one_step =  dp[i-1]+abs(h[i-1]-h[i])                
    dp[i] = min(two_step, one_step)

print(dp[N-1])