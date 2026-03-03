def solution(mats, park):
    answers = set()
    delta = [(-1, 0), (0, -1), (-1, -1)]
    row, col = len(park), len(park[0])
    for y in range(row):
        for x in range(col):
            if park[y][x] == "-1":
                flag = True
                for dx, dy in delta:
                    p = park[y + dy][x + dx]
                    if not isinstance(p, int):
                        flag = False
                        break
                if flag:
                    park[y][x] = min(park[y - 1][x - 1], park[y - 1][x], park[y][x - 1]) + 1
                else:
                    park[y][x] = 1
                answers.add(park[y][x])
                
    answer = 0
    for mat in sorted(mats):
        if mat in answers:
            answer = mat
    if answer:
        return answer
    else:
        return -1