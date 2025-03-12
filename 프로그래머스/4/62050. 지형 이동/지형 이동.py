from collections import deque


def solution(land, height):
    global answer
    answer = 0
    N = len(land)
    
    # 사다리 없이 이동할 수 있는 칸들을 같은 색깔로 묶을 맵
    MAP = [[0] * N for _ in range(N)]
    delta = [(0,1), (1,0), (0,-1), (-1,0)]
    # bfs로 사다리 없이 갈 수 있으면 같은 색으로 정의
    color = 1
    for i in range(N):
        for j in range(N):
            if not MAP[i][j]:
                queue = deque([(i,j)])
                MAP[i][j] = color
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not MAP[nx][ny] and abs(land[nx][ny] - land[x][y]) <= height:
                            MAP[nx][ny] = color
                            queue.append((nx, ny)) 
                color += 1
    
    # 사다리
    ladders = []
    for x in range(N):
        for y in range(N):
            # 오른쪽이랑 아래로만 연결할 수 있는지 확인하면 중복을 없앨 수 있음
            for dx, dy in delta[:2]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] != MAP[x][y]:
                    ladders.append((abs(land[nx][ny] - land[x][y]), (x,y), (nx,ny)))
    # 최소 비용인 사다리부터 설치
    ladders.sort(key = lambda x : x[0])
    
    # 유니온 파인드
    parent = [x for x in range(color+1)]
    
    def find(x):
        if parent[x] != x:
            return find(parent[x])
        return x
    
    def union(a, b, cost):
        global answer
        a = find(a)
        b = find(b)
        # 부모가 다른경우 사다리를 설치하고 비용추가, 부모 업데이트
        if a != b:
            answer += cost
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
    
    for cost, (x1, y1), (x2, y2) in ladders:
        a = MAP[x1][y1]
        b = MAP[x2][y2]
        union(a, b, cost)
            
    return answer