S = input()

if S[0].isupper():
  if len(S)==1:
    print("Yes")
  elif S[1:].islower():
    print("Yes")
  else:
    print("No")
else:
  print("No")