N = int(input())
A = list(map(int, input().split()))

flag = 0
cnt = 0

while flag==0:
    cnt += 1
    for i in range(N):
        if(A[i]%2==0):
            A[i] = A[i]/2
        else:
            flag = 1
            break

print( cnt -1 )