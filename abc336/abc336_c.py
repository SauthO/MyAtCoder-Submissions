N = int(input())

N = N-1

discovered = False

ans = []
ans.append(str(2*(N%5)))
i=1

while True:
    if N//5**i == 0:
        break
    else:
        ans.append(str(2*((N//5**i)%5)))
        i += 1

ans.reverse()
print(int("".join(ans)))