W, B= map(int, input().split())
S = ["w", "b", "w", "b", "w", "w", "b", "w", "b", "w", "b", "w"]
s = []
for _ in range(20):
  s += S

w_cnt = [0]*1000
b_cnt = [0]*1000

w_cnt[0] = 1

for i in range(1, len(s), 1):
  if s[i] == "w":
    w_cnt[i] = w_cnt[i-1] + 1
    b_cnt[i] = b_cnt[i-1]
  else:
    w_cnt[i] = w_cnt[i-1]
    b_cnt[i] = b_cnt[i-1] + 1

def check(w_cnt, b_cnt, W, B, Len):
  for l in range(12, Len, 1):
    for r in range(l, Len, 1):
      if w_cnt[r]- w_cnt[l-1] == W and b_cnt[r] - b_cnt[l-1] == B:
        return True
  return False
  
if check(w_cnt, b_cnt, W, B, len(s)):
  print("Yes")
else:
  print("No")
  
  