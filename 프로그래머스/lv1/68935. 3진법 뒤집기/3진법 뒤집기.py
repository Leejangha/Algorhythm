def solution(n):
    answer = 0
    tri = ''
    while n > 0:
        div = n%3
        tri += str(div)
        n //= 3
    answer = int(tri, 3)
    return answer