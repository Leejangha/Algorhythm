def solution(n):
    answer = 0
    N = str(n)
    for char in N:
        answer += int(char)

    return answer