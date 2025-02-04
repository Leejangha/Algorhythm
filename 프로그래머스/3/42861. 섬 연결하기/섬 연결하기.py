def solution(n, costs):
    answer = 0
    
    def find(x):
        if parent[x] != x:
            return find(parent[x])
        return x

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

    parent = [i for i in range(n)]

    edges = []
    
    for a, b, cost in costs:
        edges.append((cost, a, b))

    edges.sort()
    
    for edge in edges:
        cost, a, b = edge
        if find(a) != find(b):
            union(a,b)
            answer += cost

    return answer