import re
S = input()

A_pattern = "A*"
B_pattern = "B*"
C_pattern = "C*"

if S == "":
    print("Yes")
else:
    S = re.sub(A_pattern, "", S, 1)
    S = re.sub(B_pattern, "", S, 1)
    S = re.sub(C_pattern, "", S, 1)
    if S == "":
        print("Yes")
    else:
        print("No")