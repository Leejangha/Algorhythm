import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
MAP = [list(map(int, list(input()))) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 2:
            x, y = i, j
            break


delta = [(0,1), (0,-1), (1,0), (-1,0)]

visited = [[0] * m for _ in range(n)]

def bfs(x, y):
    q = deque([])
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and MAP[nx][ny] != 1:
                if MAP[nx][ny]:
                    return visited[x][y]
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

answer = bfs(x, y)


if not answer:
    print("NIE")
else:
    print("TAK")
    print(answer)
