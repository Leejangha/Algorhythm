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

# 첫번째 풀이는 value에 카운트가 들어가므로 아래 풀이가 더 해시에 적합하고 효율적인거 같음
def solution(participant, completion):
    hash_table = {}
    
    # 해시 키 값들의 총합
    hash_sum = 0
    
    # 참가자들을 해시 테이블에 저장
    for par in participant:
        p = hash(par)
        hash_table[p] = par
        # 참가자들의 키 값들을 다 더함
        hash_sum += p
    
    # 완주자들의 키 값들을 참가자들의 키 값들의 합에서 뺌
    for com in completion:
        hash_sum -= hash(com)

    # hash_sum은 완주하지 못한 참가자의 해시 키 값이 됨
    return hash_table[hash_sum]