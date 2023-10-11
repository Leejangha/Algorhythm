def solution(elements):
    SET = set()
    N = len(elements)
    elements *= 2
    for i in range(N):
        for j in range(0,N):
            SET.add(sum(elements[j:j+i+1]))
    answer = len(SET)
    return answer