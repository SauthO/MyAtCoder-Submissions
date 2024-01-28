S = input().strip()[::-1]
words = ["dream", "dreamer", "erase", "eraser"]
words = [word[::-1] for word in words]

matched = False

while len(S)>0:
  for word in words:
    if S.startswith(word):
      S = S[len(word):]
      matched = True
      break
  if not matched:
    break
  matched = False

if len(S)==0:
  print("YES")
else:
  print("NO")
  