from collections import deque

Q = int(input())
query = [ input().split() for _ in range(Q)]
T = deque()

for q in range(Q):
  if query[q][0] == "1":
    T.append(query[q][1])
    
  elif query[q][0] == "2":
    print(T[0])
    
  elif query[q][0] == "3":
    T.popleft()