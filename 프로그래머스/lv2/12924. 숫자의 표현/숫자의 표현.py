def solution(n):
    answer = 0
    k = 0
    x = 1
    while k < n:
        if (n-k) % x == 0:
            answer += 1
        k += x
        x += 1
    return answer