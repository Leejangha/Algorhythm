def quad(arr, N, x, y):
    is_zero = True
    is_one = True
    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[i][j] == 0:
                is_one = False
            else:
                is_zero = False
            if not is_zero and not is_one:
                break
    if is_zero:
        answer[0] += 1
        return
    elif is_one:
        answer[1] += 1
        return

    quad(arr, N//2, x, y)
    quad(arr, N//2, x, y+N//2)
    quad(arr, N//2, x+N//2, y)
    quad(arr, N//2, x+N//2, y+N//2)


def solution(arr):
    global answer
    answer = [0, 0]
    N = len(arr)
    quad(arr, N, 0, 0)
    return answer