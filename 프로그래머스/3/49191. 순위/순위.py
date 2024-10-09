def solution(n, results):
    answer = 0
    MAP = [[0] * (n+1) for _ in (range(n+1))]

    for result in results:
        winner = result[0]
        loser = result[1]
        MAP[winner][loser] = 1
        MAP[loser][winner] = -1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j or MAP[i][j] in [-1, 1]:
                    continue
                if MAP[i][k] == MAP[k][j] == 1:
                    MAP[i][j] = 1
                    MAP[j][i] = MAP[j][k] = MAP[k][i] = -1
    for M in MAP:
        if M.count(0) == 2:
            answer += 1
    return answer