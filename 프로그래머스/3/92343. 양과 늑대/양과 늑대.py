def solution(info, edges):
    answer = []
    # 방문한 노드를 체크할 리스트
    visited = [False] * len(info)
    
    # 깊이 우선 탐색 방법으로 이동할 수 있는 노드를 탐색
    def dfs(sheeps, wolves):
        # 양이 늑대보다 많은 경우 현재 양의 개수를 리스트에 저장
        if sheeps > wolves:
            answer.append(sheeps)
        # 늑대가 양보다 같거나 많을 경우 종료
        else:
            return
        
        for p, c in edges:
            # 부모는 방문하였지만 자식은 방문 안한 경우만 진행
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheeps + 1, wolves)
                else:
                    dfs(sheeps, wolves + 1)
                # 만약 다른 곳을 들렸다 방문 시 조건에 충족할 수 있어 false 처리
                visited[c] = False
                
    visited[0] = True
    dfs(1, 0)
    
    return max(answer)