def solution(brown, yellow):
    # xy = yellow, x >= y --> yellow >= y^2
    for y in range(1, int(yellow ** 0.5) + 1):
        # 길이는 정수
        if yellow % y == 0:
            x = yellow // y
            # 갈색은 노란색 가로 세로 합의 두배에 모서리 4를 더한 값
            if 2 * (x + y) == brown - 4:
                return [x + 2, y + 2]
    return