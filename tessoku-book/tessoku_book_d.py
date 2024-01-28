N = int(input())
ans = []
residue = N%2
N_next = int(N/2) 
ans.append(str(residue))

while N_next != 0:
  residue = N_next%2
  N_next = int(N_next/2)
  ans.append(str(residue))

  
while len(ans)<10:
  ans.append("0")

ans.reverse()
print("".join(ans))