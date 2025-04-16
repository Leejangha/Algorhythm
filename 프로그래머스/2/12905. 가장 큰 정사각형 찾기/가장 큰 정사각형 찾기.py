# from collections import defaultdict

# def solution(board):
#     DICT = defaultdict(list)
    
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j]:
#                 DICT[1].append((i,j))
    
#     delta = [(1,0), (0,1), (1,1)]
#     l = 1
#     while DICT[l]:
#         x, y = DICT[l].pop(0)
        
#         flag = 0
#         for dx, dy in delta:
#             nx, ny = x + dx, y + dy
            
#             if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
#                 if board[nx][ny] == l:
#                     flag += 1
                    
#         if flag == 3:
#             board[x][y] += 1
#             DICT[l+1].append((x,y))

#         if not DICT[l]:
#             l += 1

#     return (l-1)**2

def solution(board):
    max_s = 0
    if 1 in board[0] or 1 in list(zip(*board))[0]:
        max_s = 1
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] and board[i-1][j] and board[i][j-1] and board[i-1][j-1]:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                if board[i][j] > max_s:
                    max_s = board[i][j]
    return max_s**2
    