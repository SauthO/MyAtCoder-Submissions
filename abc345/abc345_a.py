import re

S = input()

pattern = r"<=+>"

t = re.fullmatch(pattern, S)

if t != None :
  print("Yes")
else:
  print("No")