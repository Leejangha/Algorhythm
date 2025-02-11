def solution(n, computers):
    global answer
    answer = n
    
    # 방문한 노드를 체크할 리스트
    visited = [False] * (n+1)
    
    def dfs(computers, v, visited):
        global answer
        visited[v] = True
        
        for c in range(n):
            if computers[v][c] == 1 and not visited[c]:
                answer -= 1
                dfs(computers, c, visited)
    
    for i in range(n):
        dfs(computers, i, visited)
    
    return answer

