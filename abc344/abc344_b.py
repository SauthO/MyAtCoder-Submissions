A = []
while True:
  A.append(int(input()))
  if A[-1] == 0:
    break

for i in range(1, len(A)+1, 1):
  print(A[-i])