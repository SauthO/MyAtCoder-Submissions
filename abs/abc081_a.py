n = int(input())

a = int(n/100)
b = int(n/10) -10*a
c = n - 100*a -10*b

print(a+b+c)