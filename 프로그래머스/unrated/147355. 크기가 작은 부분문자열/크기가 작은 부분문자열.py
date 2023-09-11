def solution(t, p):
    answer = 0
    P = len(p)
    T = len(t)
    for i in range(T-P+1):
        if int(t[i:i+P]) <= int(p):
            answer += 1
    return answer