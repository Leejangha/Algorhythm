def solution(keyinput, board):
    col, row = board[0]//2, board[1]//2
    x, y = 0, 0
    delta = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    for key in keyinput:
        dx, dy = delta[key]
        if -col <= x + dx <= col and -row <= y + dy <= row:
            x += dx
            y += dy
    return [x, y]