def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    for i in range(n):
        h, m = divmod(schedules[i], 100)
        h2, m2 = divmod(h * 60 + m+10, 60)
        schedules[i] = h2 * 100 + m2
    for i in range(n):
        flag = True
        for j in range(7):
            if (j + startday - 1) % 7 <= 4 and timelogs[i][j] > schedules[i]:
                flag = False
                break
        answer += flag
    return answer