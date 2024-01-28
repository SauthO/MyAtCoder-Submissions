N = int(input())
t =[]
x =[]
y =[]

go = True

for i in range(N+1):
    if i==0:
        t.append(0) 
        x.append(0)
        y.append(0)
    else:
        t_i, x_i, y_i = map(int, input().split())
        t.append(t_i) 
        x.append(x_i)
        y.append(y_i)

for i in range(N):
    d = abs(x[i+1]-x[i]) + abs(y[i+1]-y[i]) #マンハッタン距離
    T = t[i+1]-t[i] #移動に使える時間
  
    if d>T or (T-d)%2!=0:
        print("No")
        go = False
        break
    
if go:
  print("Yes")