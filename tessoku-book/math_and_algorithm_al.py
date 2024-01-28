T = int(input())
N = int(input())
L = [0]*N
R = [0]*N

for n in range(N):
  L[n], R[n] = map(int, input().split())

flag = [0]*(T+2)
for n in range(N):
  flag[L[n]] += 1
  flag[R[n]] -= 1
for t in range(1, T+1, 1):
  flag[t] += flag[t-1]
for t in range(T):
  print(flag[t])