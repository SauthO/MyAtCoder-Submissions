N, K = map(int, input().split())
cnt = 0

for i in range(1, N+1, 1):
  for j in range(1, N+1, 1):
    if K-i-j>=1 and K-i-j<=N:
      cnt += 1

print(cnt)