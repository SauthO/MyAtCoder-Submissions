S = input()
N = len(S)


alp = []

S = list(S)
cnt = [0]*27
for i in range(N):
  for j in range(97, 123):
    if S[i] == chr(j):
      cnt[j-97] += 1

c = 0

for i in cnt:
  if i > 1 :
    c += (i-1)/2*(1+i-1)

test = 0
for i in cnt:
  if i == 1:
    test += 1
if test == N:
  ans = (N-1)/2*(1+(N-1))
else:
  ans = (N-1)/2*(1+(N-1)) + 1
    
print(int(ans-c))