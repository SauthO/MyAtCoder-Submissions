A, B = map(int, input().split())
discovered = False
for i in range(A, B+1, 1):
  if(100%i==0):
    print("Yes")
    discovered = True
    break
if not discovered:
  print("No")