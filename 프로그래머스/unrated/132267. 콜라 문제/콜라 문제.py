def solution(a, b, n):
    answer = 0
    while n >= a:
        x, y = divmod(n, a)
        answer += x*b
        n = x*b + y
    return answer