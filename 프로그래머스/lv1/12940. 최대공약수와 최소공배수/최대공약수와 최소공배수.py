def solution(n, m):
    max_div = 0
    for num in range(1,min(n,m)+1):
        if n%num == 0 and m%num== 0:
            if num > max_div:
                max_div = num
    answer = [max_div, n*m//max_div]
    return answer