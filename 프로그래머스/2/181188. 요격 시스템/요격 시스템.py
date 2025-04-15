def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[1])
    i = 1
    now = targets[0][1]
    while i < len(targets):
        if targets[i][0] >= now:
            answer += 1
            now = targets[i][1]
        i += 1
        
    return answer