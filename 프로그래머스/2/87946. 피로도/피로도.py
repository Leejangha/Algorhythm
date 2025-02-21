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


# # 2. 백트래킹
# def solution(k, dungeons):
#     answer = -1
#     N = len(dungeons)
#     visited = [False] * N
    
#     def back(k, cnt, dungeons):
#         nonlocal answer
#         # 탐험한 최대 던전 수 업데이트
#         if cnt > answer:
#             answer = cnt
        
#         # 던전의 방문여부를 기록해야 하므로 인덱스를 같이
#         for i, (need, spend) in enumerate(dungeons):
#             # 던전의 필요 피로도보다 많이 남아있고 아직 방문하지 않은 경우
#             if k >= need and not visited[i]:
#                 # 방문처리
#                 visited[i] = True
#                 # 피로도를 깎고 탐험한 던전수를 늘려서 아직 탐험하지 않은 다음 던전들을 탐험
#                 back(k - spend, cnt + 1, dungeons)
#                 # 뒤에 던전을 먼저 탐험한 뒤에 앞에 던전을 탐험할 수 있으니 재방문처리
#                 visited[i] = False

#     back(k, 0, dungeons)
#     return answer