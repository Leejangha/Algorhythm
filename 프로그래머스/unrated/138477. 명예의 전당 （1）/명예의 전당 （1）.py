def solution(k, score):
    answer = []
    vic = []    # 명예의 전당
    for s in score:
        if len(vic) < k:    # 전당이 k개가 될때 까지는 전부 올림
            vic.append(s)
            vic.sort(reverse=True) # 전당의 점수를 내림차순으로 정렬
        else:
            if s > vic[-1]: # 전당의 최소점보다 점수가 높을 경우
                vic.pop()   # 최소점을 내림
                vic.append(s)   # 가수의 점수를 올림
            vic.sort(reverse=True) # 내림차순으로 정렬
        answer.append(vic[-1])  # 최소점을 기록
    return answer