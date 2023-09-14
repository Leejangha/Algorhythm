def solution(k, m, score):
    score.sort(reverse=True)
    answer = sum(score[m-1::m])*m
    return answer