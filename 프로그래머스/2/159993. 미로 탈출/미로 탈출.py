from collections import deque

# 너비 우선 탐색으로 최단거리 찾기
def bfs(start, maps, row, col):
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([start])
    # 방문한 칸을 체크할 2차원 리스트
    visited = [[0]*col for _ in range(row)]
    # 시작점 방문표시
    visited[start[0]][start[1]] = 1
    
    # 다음 방문할 칸이 없어질때 까지
    while queue:
        x, y = queue.popleft()
        # 레버에 도착하면 이동한 최단거리 반환
        if maps[x][y] == "L":
            # 시작을 1로 했으므로 1을 빼줌
            return visited[x][y] -1
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            # 다음 이동할 칸이 미로안이고, 벽이 아니고, 방문한 적이 없는 경우에만 이동
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] != "X" and visited[nx][ny] == 0:
                # 이동한 칸은 전 칸까지 이동한 거리 + 1
                visited[nx][ny] = visited[x][y] + 1
                # 이동한 칸에서 또 이동을 해야하므로 큐에 넣음
                queue.append((nx,ny))
    return False
    

def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    for x in range(row):
        for y in range(col):
            # 문제에서 레버를 당기러 갈때 출구를 지날 수 있으므로, 출구에 처음 도착이 종료 조건이 아님
            # 시작부터 레버까지 최단거리 + 출구에서 레버까지 최단거리가 정답
            if maps[x][y] in ["S", "E"]:
                '''
                레버까지 갈 수 있는지 없는지 확인하는 플래그
                그냥 answer==0 으로 확인할 경우, 시작부터 레버까지는 갈 수 있지만 
                도착에서 못 가는 경우를 예외처리 하지 못함
                '''
                flag = answer
                answer += bfs((x,y), maps, row, col)
                # 레버까지 갈 수 없으면 False를 반환하여 정답의 변화가 없으므로 -1 반환
                if answer == flag:
                    return -1

    return answer