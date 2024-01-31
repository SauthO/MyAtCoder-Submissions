N, Q = map(int, input().split())
query = [input().split() for _ in range(Q)]

d = [(i, 0) for i in range(1, N+1, 1)][::-1]

for q in range(Q):
    if query[q][0] == '1':
        c = query[q][1]
        x = d[-1][0]
        y = d[-1][1]
        
        if c == 'R':
            x += 1
            
        if c == 'L':
            x -= 1
            
        if c == 'U':
            y += 1
        
        if c == 'D':
            y -= 1
        d.append((x, y))
        
    if query[q][0] == '2':
        p = int(query[q][1])
        print(d[-p][0], d[-p][1])
        