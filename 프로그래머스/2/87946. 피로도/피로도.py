# 1. 완전탐색
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    
    # 던전들의 모든 순열을 생성후 완전탐색
    for perm in permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0
        
        for need, spend in perm:
            if hp >= need:
                hp -= spend
                cnt += 1
            else:
                break
        
        if cnt > answer:
            answer = cnt
    
    return answer