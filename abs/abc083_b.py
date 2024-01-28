N, A, B = map(int, input().split())
sum_part = 0
sum = 0
n4 = 0
n3 = 0
n2 = 0
n1 = 0
n0 = 0

for i in range(1, N+1, 1):
    n4 = int(i/1e4)
    n3 = int(i/1e3) - n4*1e1
    n2 = int(i/1e2) - n4*1e2 -n3*1e1
    n1 = int(i/1e1) - n4*1e3 - n3*1e2 - n2*1e1
    n0 = i - n4*1e4 - n3*1e3 - n2*1e2 - n1*1e1
    sum_part = n4 + n3 + n2 + n1 + n0
    if sum_part>=A and sum_part<=B:
        sum += i

print(sum)
  