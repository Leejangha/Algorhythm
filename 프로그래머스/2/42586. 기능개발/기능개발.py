from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([])
    
    for p, s in zip(progresses, speeds):
        p = 100 - p
        if p % s == 0:
            queue.append(p//s)
        else:
            queue.append(p//s + 1)
    
    now = queue.popleft()
    cnt = 1
    
    while queue:
        if not queue:
            answer.append(cnt)
            now = queue.popleft()
            cnt = 1
        else:
            if queue[0] <= now:
                queue.popleft()
                cnt += 1
            else:
                answer.append(cnt)
                now = queue.popleft()
                cnt = 1

    answer.append(cnt)
    return answer