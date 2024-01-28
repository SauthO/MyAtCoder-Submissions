s = str(input())
if len(s)>1:
  if s[0].isupper() and s[1:].islower():
    print("Yes")
  else:
    print("No")
if len(s)==1:
  if s[0].isupper():
    print("Yes")
  else:
    print("No")