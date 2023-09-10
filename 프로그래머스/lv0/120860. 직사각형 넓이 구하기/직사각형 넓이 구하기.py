def solution(dots):
    x1 = dots[0][0]
    y1 = dots[0][1]
    for x, y in dots[1:]:   # x2, y2부터 x1, y1과 비교
        if x != x1: # x1과 다를경우
            row = abs(x-x1) # 밑변의 길이를 구함
        if y != y1: # y1과 다를경우
            col = abs(y-y1) # 높이를 구함
    answer = row*col    # 넓이를 계산
    return answer