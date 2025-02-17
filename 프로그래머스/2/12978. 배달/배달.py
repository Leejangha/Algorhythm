from collections import defaultdict


def solution(N, road, K):
    graph = defaultdict(list)
    
    for a, b, c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))

    distance = [float("inf")] * (N+1)
    distance[1] = 0
    
    for _ in range(N):
        for a in range(1, N+1):
            for b, c in graph[a]:
                if distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c
                    
    answer = len(list(x for x in distance if x <= K))

    return answer