def solution(n):
    global answer
    answer = 0
    board = [0]*n
    
    def back(row, col):
        # 이전에 놓은 퀸들의 행 탐색
        for i in range(row):
            # 같은 열이거나 대각선인 경우 돌아감
            if board[i] == col or row - i == abs(board[i] - col):
                return False
        return True
    
    def nqueen(row):
        global answer
        # 마지막 행까지 놓았다면 결과 + 1
        if row == n:
            answer += 1
            return
        
        for col in range(n):
            board[row] = col
            if back(row, col):
                # 이번 row의 col에 놓아도 되면 다음 행으로 내려간다
                nqueen(row + 1)
        
    nqueen(0)
    return answer