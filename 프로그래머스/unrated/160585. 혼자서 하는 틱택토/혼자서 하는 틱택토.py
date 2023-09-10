def solution(board):
    answer = 1
    num_O = 0
    num_X = 0
    num_ = 0
    board_r = list(zip(*board))
    print(board_r)
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'O':
                num_O += 1
            elif board[x][y] == 'X':
                num_X += 1
            else:
                num_ += 1
    if num_X > num_O:
        answer = 0
    elif num_O - num_X > 1:
        answer = 0
    else:
        cnt_O = 0
        cnt_X = 0
        cnt_O_r = 0
        cnt_X_r = 0
        for x in range(3):
            if board[x][x] == 'O':
                cnt_O += 1
            elif board[x][x] == 'X':
                cnt_X += 1
            if board[x][2-x] == 'O':
                cnt_O_r += 1
            elif board[x][2-x] == 'X':
                cnt_X_r += 1
            if board[x].count('O') == 3 or board_r[x].count('O') == 3 or cnt_O == 3 or cnt_O_r == 3:
                if num_O == num_X:
                    answer = 0
            elif board[x].count('X') == 3 or board_r[x].count('X') == 3 or cnt_X == 3 or cnt_X_r == 3:
                if num_O > num_X:
                    answer = 0
    return answer