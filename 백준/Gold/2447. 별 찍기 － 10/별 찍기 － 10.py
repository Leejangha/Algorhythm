N = int(input())

MAP = [[0] * N for _ in range(N)]

def star(x, y, N):
    if N == 1 and MAP[x][y] == 0:
        MAP[x][y] = '*'
        return
    
    n = N // 3
    if 1*n <= x%N < 2*n and 1*n <= y%N < 2*n and MAP[x][y] == 0:
        MAP[x][y] = ' '
        
    else:
        star(x, y, n)

for x in range(N):
    for y in range(N):
        star(x, y, N)

for m in MAP:
    print(''.join(m))
