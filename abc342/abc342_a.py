s = list(map(str, input()))
r = [None]*len(s)

for i in range(len(s)):
  if i == len(s)-1:
    if s[i] != s[0]:
      r[i] = "1"
    else:
      r[i] = "0"
  
  else:
    if s[i] != s[i+1] :
      r[i] = "1"
    else:
      r[i] = "0"
  
cnt = 0

if r[0] == "1" and r[-1] == "1":
  print(1)

else:
  for i in range(len(s)):
    if r[i] == "1":
      cnt += 1
    if cnt == 2:
      print(i+1)
      break