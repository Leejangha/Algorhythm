def solution(dirs):
    answer = 0
    # 명령어에 따른 이동을 정의
    delta = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    # 11 * 11 크기의 좌표평면 정의 (-5 ~ 5), 각 좌표에서 수행한 명령을 저장해야 하므로 빈 문자열('')으로 정의 
    MAP = [['']*11 for _ in range(11)]
    # 초기좌표 설정
    x = y = 5

    for dr in dirs:
        dx, dy = delta[dr]
        # 이동할 좌표
        nx, ny = x + dx, y + dy
        # 이동할 좌표가 경계 안쪽일 경우에만 이동
        if 0 <= nx < 11 and 0 <= ny < 11:
            # 현재 위치에서 같은 명령을 수행한 적이 없는 경우 명령 추가
            if dr not in MAP[x][y]:
                MAP[x][y] += dr
                # 처음 이동하는 길인 경우 길이 +1
                if dr == 'U' and 'D' not in MAP[nx][ny]:
                    answer += 1
                elif dr == 'D' and 'U' not in MAP[nx][ny]:
                    answer += 1
                elif dr == 'R' and 'L' not in MAP[nx][ny]:
                    answer += 1
                elif dr == 'L' and 'R' not in MAP[nx][ny]:
                    answer += 1
            
            # 이동
            x = nx
            y = ny
    
    return answer