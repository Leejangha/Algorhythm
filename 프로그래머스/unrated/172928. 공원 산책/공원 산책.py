delta = {'E': (0,1), 'W': (0,-1), 'N': (-1,0), 'S': (1,0)}


def solution(park, routes):
    H = len(park)
    W = len(park[0])
    commands = []
    for route in routes:
        commands.append([delta[route[0]], int(route[2])])
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x, y = i, j
                for (dx, dy), n in commands:
                    go_lst = []
                    for k in range(1, n+1):
                        nx, ny = x+dx*k, y+dy*k
                        if 0 <= nx < H and 0 <= ny < W:
                            go_lst.append(park[nx][ny])
                    if len(go_lst) == n and 'X' not in go_lst:
                        x, y = x+dx*n, y+dy*n        
    answer = [x, y]
    return answer