def solution(info, edges):
    global answer
    answer = 0
    graph =  [[] for _ in range(len(info))]
    for a, b in edges:
        graph[a].append(b)
        
    def dfs(now, nxt, sheep, wolf):
        global answer
        
        if info[now] == 0:
            sheep += 1
            answer = max(answer, sheep)
        else:
            wolf += 1
        
        if sheep <= wolf:
            return 0
        
        for n in nxt:
            for node in graph[n]:
                if node not in nxt:
                    nxt.append(node)
                    dfs(node, nxt, sheep, wolf)
                    nxt.pop()
    
    dfs(0, [0], 0, 0)
    return answer