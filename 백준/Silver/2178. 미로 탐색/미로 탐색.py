import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, list(input()))) for _ in range(N)]

delta = [(0,1), (0,-1), (1,0), (-1,0)]

visited = [[0] * M for _ in range(N)]

q = deque([])
q.append((0,0))
visited[0][0] = 1

while q:
    x, y = q.popleft()
    
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and MAP[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

print(visited[N-1][M-1])