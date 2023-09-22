import heapq

INF = int(1e9)


def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]


    for fare in fares:
        v, e, w = fare
        graph[v].append((e,w))
        graph[e].append((v,w))

    def dijkstra(start):
        distance = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance

    min_cost = dijkstra(s)[a] + dijkstra(s)[b]
    for i in range(n+1):
        min_cost = min(min_cost, dijkstra(s)[i]+ dijkstra(i)[a] + dijkstra(i)[b])
    return min_cost