def solution(lottos, win_nums):
    win = 0
    for lotto in lottos:
        if lotto in win_nums:
            win += 1
    cnt = lottos.count(0)
    Max = min(6, 7-(win+cnt))
    Min = min(6, 7-win)
    answer = [Max, Min]
    return answer