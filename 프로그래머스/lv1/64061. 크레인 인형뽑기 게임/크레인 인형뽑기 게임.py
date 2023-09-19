def solution(board, moves):
    answer = 0
    board = list(map(list, (zip(*board))))
    for i in range(len(board)):
        while 0 in board[i]:
            board[i].remove(0)
    stack = []
    for move in moves:
        if board[move-1]:
            doll = board[move-1].pop(0)
            if not stack:
                stack.append(doll)
            else:
                if stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
    return answer