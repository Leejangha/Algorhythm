# def solution(n):
#     global answer
#     answer = 0
#     board = [0]*n
    
#     def back(row, col):
#         # 이전에 놓은 퀸들의 행 탐색
#         for i in range(row):
#             # 같은 열이거나 대각선인 경우 돌아감
#             if board[i] == col or row - i == abs(board[i] - col):
#                 return False
#         return True
    
#     def nqueen(row):
#         global answer
#         # 마지막 행까지 놓았다면 결과 + 1
#         if row == n:
#             answer += 1
#             return
        
#         for col in range(n):
#             board[row] = col
#             if back(row, col):
#                 # 이번 row의 col에 놓아도 되면 다음 행으로 내려간다
#                 nqueen(row + 1)
        
#     nqueen(0)
#     return answer

def solution(n):
    check_col = [False] * 100; check_d1 = [False] * 100; check_d2 = [False] * 100
    def process(row):
        answer = 0
        if row == n+1:
            return 1
        for i in range(1,n+1):
            d1 = row+i; d2 = n + (row - i)
            if check_col[i] == False and check_d1[d1] == False and check_d2[d2] == False:
                check_col[i] = True; check_d1[d1] = True; check_d2[d2] = True
                answer += process(row+1)
                check_col[i] = False; check_d1[d1] = False; check_d2[d2] = False
        return answer
    answer = process(1)
    return answer