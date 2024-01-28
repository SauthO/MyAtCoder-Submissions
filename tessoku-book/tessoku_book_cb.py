N = int(input())
A = list(map(int, input().split()))
discovered = False

for i in range(N):
  for j in range(N):
    if j==i:
      break
    for k in range(N):
      if k==i or k==j:
        break
      if A[i]+A[j]+A[k] == 1000:
        print("Yes")
        discovered = True
        break
    if discovered:
      break
  if discovered:
    break
if not discovered:
  print("No")