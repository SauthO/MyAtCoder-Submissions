S = list(input())

flg = False

for i in range(len(S)):
  if (S[i]=="|") and (not flg):
    flg = True
  
  elif (S[i]=="|") and (flg):
    S[i] = ""
    flg = False
  
  if flg:
    S[i] = ""

print("".join(S))