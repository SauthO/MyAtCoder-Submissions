N = int(input())

def f(x):
  return x**3 + x

L = 0.0
R = 100.0

for _ in range(20):
  M = (L+R)/2.0
  if f(M) < N:
    L = M
  elif f(M) > N:
    R = M

print(M)