from itertools import permutations


def solution(k, dungeons):
    answer = -1
    
    for perm in permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0
        
        for need, spend in perm:
            if hp >= need:
                hp -= spend
                cnt += 1
        
        if cnt > answer:
            answer = cnt
    
    return answer