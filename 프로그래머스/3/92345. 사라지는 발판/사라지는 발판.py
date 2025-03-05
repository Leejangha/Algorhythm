def solution(board, aloc, bloc):
    row = len(board)
    col = len(board[0])
    delta = [(0,1), (0,-1), (1,0), (-1,0)]

    def back(board, turn, aloc, bloc):
        if turn % 2 == 0:
            r, c = aloc
        else:
            r, c = bloc

        win, loss = [], []
        
        nxt = []
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and board[nr][nc]:
                nxt.append((nr, nc))
                
        if not nxt:
            return turn % 2 != 0, turn
        
        if aloc == bloc:
            return turn % 2 == 0, turn + 1
        
        board[r][c] = 0
        for nr, nc in nxt:
            if turn % 2 == 0:
                a_win, cnt = back(board, turn + 1, [nr, nc], bloc)
            else:
                a_win, cnt = back(board, turn + 1, aloc, [nr, nc])
                
        
            if (turn % 2 == 0 and a_win) or (turn % 2 == 1 and not a_win):
                win.append(cnt)
            else:
                loss.append(cnt)
        board[r][c] = 1
        
        if win:
            return turn % 2 == 0, min(win)
        else:
            return turn % 2 != 0, max(loss)
    
    _, answer = back(board, 0, aloc, bloc)

    return answer