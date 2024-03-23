N, K = map(int, input().split())
A = list(map(int, input().split()))

A_part = 0
A = set(A)

for a in A:
  if a <= K:
    A_part += a

K_sum = (1+K) * K//2 

print(K_sum - A_part )