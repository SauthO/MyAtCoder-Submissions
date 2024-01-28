N = int(input())

Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

QA_min = 1e10

for n in range(N):
    if A[n]!=0:
        QA_min = min(QA_min, int(Q[n]/A[n]))
cnt = 0

for a in range(QA_min+1):
    b = 1e10
    for n in range(N):
        if Q[n]-a*A[n] >= 0 and B[n]!=0:
            b = min( b, (Q[n]-a*A[n])//B[n] )
    cnt = max( cnt, a+b )
print(cnt)