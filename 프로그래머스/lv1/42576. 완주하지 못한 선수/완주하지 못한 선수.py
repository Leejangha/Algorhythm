def solution(participant, completion):
    answer = ''
    par = sorted(participant)
    com = sorted(completion)
    for i in range(len(com)):
        if com[i] != par[i]:
            answer = par[i]
            break
    if not answer:
        answer = par[-1]
    return answer