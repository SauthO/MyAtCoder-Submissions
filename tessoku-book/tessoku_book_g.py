D = int(input())
N = int(input())
L = [0]*N
R = [0]*N
for n in range(N):
  L[n], R[n] = map(int, input().split())
  
joiner = [0]*(D+2)
for n in range(N):
  joiner[L[n]] += 1
  joiner[R[n]+1] -= 1

for d in range(1, D+1, 1):
  joiner[d] += joiner[d-1]

for d in range(1, D+1, 1):
  print(joiner[d])
    
