def solution(friends, gifts):
    n = len(friends)
    lists = [[0] * n for _ in range(n)]
    point = [0] * n
    res = [0] * n

    for gift in gifts:
        giver, receiver = gift.split()
        row = friends.index(giver)
        col = friends.index(receiver)
        lists[row][col] += 1

    for i in range(n):
        point[i] += sum(lists[i])
        point[i] -= sum(list(zip(*lists))[i])

    row = 0
    while row < n-1:
        for col in range(row+1, n):
            if lists[row][col] > lists[col][row]:
                res[row] += 1
            elif lists[row][col] < lists[col][row]:
                res[col] += 1
            else:
                if point[row] > point[col]:
                    res[row] += 1
                elif point[row] < point[col]:
                    res[col] += 1
        row += 1

    return max(res)
