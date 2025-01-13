def solution(board, moves):
    answer = 0

    # 보드가 행 단위 이므로 열 단위로 변경
    board = list(map(list, (zip(*board))))
    
    # 바구니의 0을 제거
    for i in range(len(board)):
        while 0 in board[i]:
            board[i].remove(0)

    stack = []
    for move in moves:
        # 해당 위치에 인형이 남아 있을 경우에만 옮김
        if board[move-1]:
            # 인형이 위에서부터 정렬되어 있으므로 0번 인덱스를 옮김
            doll = board[move-1].pop(0)
            if not stack:
                stack.append(doll)
            else:
                # 바구니의 제일 위 인형과 옮긴 인형이 같을 경우 바구니 제일 위 인형을 제거하고 2점 추가
                if stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
    return answer