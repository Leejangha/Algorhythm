def solution(n, lost, reserve):
    inter = set(reserve) & set(lost)
    reserve = list(set(reserve) - inter)
    lost = list(set(lost) - inter)
    for r in reserve:
        if (r-1) in lost:
            lost.remove(r-1)
            continue
        elif (r+1) in lost:
            lost.remove(r+1)
    answer = n - len(lost)
    return answer