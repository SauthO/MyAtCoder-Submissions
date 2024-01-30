N = int(input())
N = bin(N)
cnt = 0
if N[len(N)-1] == "1":
    print(0)
else:
    for i in reversed(range(len(N))):
        if N[i] == "0":
            cnt += 1
        else:
            break
    print(cnt)