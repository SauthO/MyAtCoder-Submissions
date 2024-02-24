N = int(input())
S = list(map(str, input()))
Q = int(input())

c = [None]*Q
d = [None]*Q

for i in range(Q):
  c[i], d[i] = map(str, input().split())

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = alphabet

for i in range(Q):
  result = result.replace(c[i], d[i])

mydict = {}

for i in range(len(alphabet)):
  mydict[alphabet[i]] = result[i]

for i in range(len(S)):
  S[i] = mydict[S[i]]
print("".join(S))