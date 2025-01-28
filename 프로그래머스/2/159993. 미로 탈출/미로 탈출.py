from collections import deque

def bfs(start, maps, row, col):
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([start])
    visited = [[0]*col for _ in range(row)]
    visited[start[0]][start[1]] = 1
    
    while queue:
        x, y = queue.popleft()
        if maps[x][y] == "L":
            return visited[x][y] -1
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] != "X" and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
    return False
    

def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    for x in range(row):
        for y in range(col):
            if maps[x][y] in ["S", "E"]:
                flag = answer
                answer += bfs((x,y), maps, row, col)
                if answer == flag:
                    return -1

    return answer