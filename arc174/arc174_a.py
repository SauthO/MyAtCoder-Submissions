N, C = map(int, input().split())
A = list(map(int, input().split()))

A.append(0)

if C < 1:
  for i in range(N+1):
    A[i] = -A[i]

S = [None]*(N+1)
S[0] = A[0]
for i in range(1, N+1, 1):
  S[i] = S[i-1] + A[i]

S_dp = [None]*(N+1)
S_dp[0] = A[0]
r = [0]*(N+1)
l = [0]*(N+1)

S_dp_max = -1

for i in range(1, N+1, 1):
  if A[i] > S_dp[i-1] + A[i]:
    S_dp[i] = A[i]
    r[i] = i
    l[i] = i
  else:
    S_dp[i] = S_dp[i-1] + A[i]
    r[i] = i
    l[i] = l[i-1]
  
i_max = 0

for i in range(N+1):
  if S_dp_max < S_dp[i]:
    S_dp_max = S_dp[i]
    i_max = i
  #print("S_dp_max", S_dp_max)
  #print("S_dp", S_dp[i])
  #print()
#print(i_max)

if C < 1:
  S_dp_max = -S_dp_max
  for i in range(N):
    A[i] = -A[i]
    S[i] = -S[i]

#print(S_dp_max)
#print(i_max)

if l[i_max] == 0 and r[i_max] == N:
    print(S_dp_max*C)

elif l[i_max] == 0 and r[i_max] != N:
  print(S_dp_max*C + S[N-1] - S[r[i_max]])

elif l[i_max] !=0 and r[i_max] == N:
  print(S[l[i_max]-1] + S_dp_max*C)

else:
  print(S[l[i_max]-1] + S_dp_max*C + S[N-1] - S[r[i_max]])
  