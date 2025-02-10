from collections import deque

# 너비 우선 탐색으로 최단거리 탐색
def bfs(start, maps, n, m):
    delta = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque([start])
    # 방문한 칸을 체크할 2차원 리스트
    visited = [[0] * m for _ in range(n)]
    # 시작점 방문표시
    visited[start[0]][start[1]] = 1
    
    # 다음 방문할 칸이 없어질때 까지
    while queue:
        x, y = queue.popleft()
        # 적 팀의 진영에 도착하면 최단거리 반환
        if (x,y) == (n-1,m-1):
            return visited[x][y]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            # 다음 이동할 칸이 맵 안이고 벽이 아니고 방문한 적이 없을 경우 이동
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                # 이동 전 칸까지의 이동거리 + 1
                visited[nx][ny] = visited[x][y] + 1
                # 이동 후 다음 칸으로 또 이동해야 함
                queue.append((nx,ny))
    # 적 팀의 진영에 도착하지 못할 경우 -1 반환
    return -1


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs((0,0), maps, n, m)
    return answer
