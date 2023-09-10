def solution(board):
    answer = 0
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] % 2 == 1:
                for k in range(i-1, i+2):
                    for r in range(j-1, j+2):
                        if 0 <= k < n and 0 <= r < n:
                            board[k][r] += 2

    for i in range(n):
        answer += board[i].count(0)

    return answer
