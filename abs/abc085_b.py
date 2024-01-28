N = int(input())
d = [int(input()) for _ in range(N)]
d.sort(reverse=True)

cnt=1

for i in range(N-1):
  if(d[i]>d[i+1]):
    cnt += 1

print(cnt)