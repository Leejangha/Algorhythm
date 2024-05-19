from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([])
    
    for p, s in zip(progresses, speeds):
        a, b = divmod(100-p, s)
        if b != 0:
            a += 1
        queue.append(a)

    cnt = 0
    while queue:
        d = queue.popleft()
        cnt += 1
        
        if queue:
            while queue[0] <= d:
                queue.popleft()
                cnt += 1
                
                if not queue:
                    break
            
        answer.append(cnt)
        cnt = 0

    return answer