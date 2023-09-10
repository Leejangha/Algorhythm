def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if not signs[i]:
            signs[i] = -1
        answer += absolutes[i] * signs[i]
    return answer