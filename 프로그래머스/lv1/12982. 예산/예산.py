def solution(d, budget):
    answer = len(d)
    d.sort(reverse=True)
    max_b = sum(d)
    if max_b <= budget:
        return answer
    for num in d:
        max_b -= num
        answer -= 1
        if max_b > budget:
            continue
        else:
            break
    return answer