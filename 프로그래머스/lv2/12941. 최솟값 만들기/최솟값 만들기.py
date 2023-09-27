def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    for l in zip(A, B):
        answer += l[0]*l[1]
    return answer