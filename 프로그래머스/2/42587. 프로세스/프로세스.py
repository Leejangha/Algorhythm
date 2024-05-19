from collections import deque

def solution(priorities, location):
    q = deque([])
    stack = []
    
    for i, p in enumerate(priorities):
        q.append((p, i))

    while q:
        now = q.popleft()
        
        if not q:
            stack.append(now)
            break
        
        if now[0] >= max(q)[0]:
            stack.append(now)
        else:
            q.append(now)
            
    for i, s in enumerate(stack, 1):
        if s[1] == location:
            answer = i
    return answer