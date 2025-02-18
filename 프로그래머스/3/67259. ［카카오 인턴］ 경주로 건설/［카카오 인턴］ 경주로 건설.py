from collections import deque


def solution(board): 
    N = len(board)

    # 최소 건설 비용 초기화
    answer = float("inf")

    # 어느 방향에서 왔는지 알아야 하므로 인덱스까지 정의
    delta = [(-1,0,0), (0,-1,1), (1,0,2), (0,1,3)]
    
    # 이전 방향별로 최소 비용 계산
    costs = [[[float("inf")] * N for _ in range(N)] for _ in range(4)]
    
    # 시작 지점 비용 초기화
    for i in range(4):
        costs[i][0][0] = 0
    
    # 시작 지점은 이전 방향이 없으므로 -1
    queue = deque([(-1, 0, 0, 0)])
    
    while queue:
        i, x, y, cost = queue.popleft()
        
        # 도착점에 도착했을 때 적은 비용으로 업데이트
        if x == N-1 and y == N-1 and answer > cost:
            answer = cost
        
        for dx, dy, dir_ in delta:
            nx , ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                # 이전 방향과 진행 방향이 같거나 시작점에서 온 경우 직선도로 
                if i == dir_ or i == -1:
                    n_cost = 100
                # 방향이 달라지는 경우 코너
                else: n_cost = 600
                
                # 이동한 지점까지 건설 비용이 적어지면 업데이트
                if costs[dir_][nx][ny] > cost + n_cost:
                    costs[dir_][nx][ny] = cost + n_cost

                    # 비용이 적게 건설된 지점부터 다시 이동
                    queue.append((dir_, nx, ny, cost + n_cost))

    return answer