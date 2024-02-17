H, W, N = map(int, input().split())
T = input()
S = [ [None for _ in range(W)] for _ in range(H) ]
for i in range(H):
  s = input()
  for j in range(W):
    S[i][j] = s[j]

cnt = 0

for i in range(1, H-1, 1):
  for j in range(1, W-1, 1):
    now_i = i
    now_j = j
    if(S[now_i][now_j]=="#"):
      continue
    
    for n in range(N):
      if T[n] == "L":
        now_j -= 1
        
      elif T[n] == "R":
        now_j += 1
        
      elif T[n] == "U":
        now_i -= 1
      
      elif T[n] == "D":
        now_i += 1
        
      if S[now_i][now_j] == "#":
        break
      if n == N-1:
        cnt += 1
print(cnt)