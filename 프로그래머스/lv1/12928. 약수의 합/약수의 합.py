def solution(n):
    answer = 0
    divisor = 1

    while divisor <= n:
        if n % divisor == 0:
            answer += divisor
        divisor += 1

    return answer