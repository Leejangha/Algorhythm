# def solution(participant, completion):
#     DICT = {} 
#     for com in completion:
#         c = hash(com)
#         if c not in DICT:
#             DICT[c] = 1
#         else:
#             DICT[c] += 1
    
#     for par in participant:
#         p = hash(par)
        
#         if p not in DICT or DICT[p] == 0:
#             return par
#         else:
#             DICT[p] -= 1
#     return

def solution(participant, completion):
    DICT = {}
    hash_sum = 0
    
    for par in participant:
        p = hash(par)
        DICT[p] = par
        hash_sum += p
    
    for com in completion:
        hash_sum -= hash(com)

    return DICT[hash_sum]