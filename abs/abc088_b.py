N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

Alice = 0
Alice_counter = 0
Bob = 0

for i in range(N):
    if(Alice_counter==0):
        Alice += a[i]
        Alice_counter = 1
    else:
        Bob += a[i]
        Alice_counter = 0
        
print(Alice - Bob)