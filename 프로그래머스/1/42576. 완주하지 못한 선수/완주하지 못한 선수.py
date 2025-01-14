# def solution(participant, completion):
#     answer = ''
#     par = sorted(participant)
#     com = sorted(completion)
#     for i in range(len(com)):
#         if com[i] != par[i]:
#             answer = par[i]
#             break
#     if not answer:
#         answer = par[-1]
#     return answer
def solution(participant, completion):
    DICT = {} 
    for com in completion:
        c = hash(com)
        if c not in DICT:
            DICT[c] = 1
        else:
            DICT[c] += 1
    
    for par in participant:
        p = hash(par)
        if p not in DICT or DICT[p] == 0:
            return par
        else:
            DICT[p] -= 1
    return