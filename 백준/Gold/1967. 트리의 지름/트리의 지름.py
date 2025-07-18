import sys

N = int(sys.stdin.readline())
trees = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    trees[a].append((b,c))
    trees[b].append((a,c))

visited = [0]*(N+1)
answer = [0]*(N+1)

def dfs(trees, start_node, visited):
    stack = [start_node]
    
    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True
               
        for next, c in trees[now]:
            if trees[next] and not visited[next]:
                stack.append(next)
                answer[next] += answer[now] + c

dfs(trees, 1, visited)

start_node = answer.index(max(answer))
visited = [0]*(N+1)
answer = [0]*(N+1)

dfs(trees, start_node, visited)

print(max(answer))
