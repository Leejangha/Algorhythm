from collections import defaultdict


def solution(N, road, K):
    # 인접 리스트 만들기
    graph = defaultdict(list)
    
    # 무방향 그래프
    for a, b, c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))

    # 거리 배열 초기화
    distance = [float("inf")] * (N+1)
    distance[1] = 0
    
    # 노드 수 만큼 반복
    for _ in range(N):
        for a in range(1, N+1):
            for b, c in graph[a]:
                 # 현재 노드 a를 거쳐 b로 가는 경로의 거리가 기존의 b까지의 거리보다 짧은 경우
                if distance[a] + c < distance[b]:
                    # 최단거리 갱신
                    distance[b] = distance[a] + c
    
    # K 시간 이하로 배달이 가능한 마을의 수
    return len(list(x for x in distance if x <= K))