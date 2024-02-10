Q = int(input())

query = [ [None for _ in range(2)] for _ in range(Q) ]

for i in range(Q):
  query[i][0], query[i][1] = map(int, input().split())

A = []

for i in range(Q):
  
  if query[i][0] == 1:
    A.append(query[i][1])
  
  if query[i][0] == 2:
    print(A[-query[i][1]])