from collections import deque


def solution(n, wires):
    answer = float("inf")
    trees = [[] for _ in range(n+1)]
    for wire in wires:
        trees[wire[0]].append(wire[1])
        trees[wire[1]].append(wire[0])

    def bfs(start, no, n):
        q = deque()
        q.append(start)
        visited = [False] * (n+1)
        while q:
            now = q.popleft()
            visited[now] = True
            for next in trees[now]:
                if next != no and not visited[next]:
                    visited[next] = True
                    q.append(next)
        return visited.count(True)

    for wire in wires:
        answer = min(answer, abs(bfs(wire[0], wire[1], n) - bfs(wire[1], wire[0], n)))
    return answer

