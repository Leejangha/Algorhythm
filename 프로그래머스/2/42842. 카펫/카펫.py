def solution(brown, yellow):
    for y in range(1, int(yellow ** 0.5) + 1):
        if yellow % y == 0:
            x = yellow // y
            if 2 * (x + y) == brown - 4:
                return [x + 2, y + 2]
    return