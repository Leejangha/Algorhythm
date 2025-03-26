from collections import deque
import sys

N, M, T = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

queue = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

queue.append((0,0,0))
for i in range(2):
    visited[i][0][0] = 1

delta = [(1,0), (-1,0), (0,1), (0,-1)]

while queue:
    flag, x, y = queue.popleft()

    if x == N-1 and y == M-1:
        break

    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < N and 0 <= ny < M and not visited[flag][nx][ny]:
            if not flag and MAP[nx][ny] == 1:
                continue
            
            nflag = flag

            if MAP[nx][ny] == 2:
                nflag = 1

            visited[nflag][nx][ny] = visited[flag][x][y] + 1
            queue.append((nflag, nx, ny))

min_time = float('inf')  
for f in range(2):
    time = visited[f][N-1][M-1]
    if time and time <= T+1:
        min_time = min(min_time, time)

print(min_time-1 if min_time != float('inf') else 'Fail')
