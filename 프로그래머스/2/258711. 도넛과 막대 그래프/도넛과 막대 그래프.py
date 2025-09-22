from collections import defaultdict, deque

def solution(edges):
    in_edges = defaultdict(list)
    out_edges = defaultdict(list)
    for a, b in edges:
        out_edges[a].append(b)
        in_edges[b].append(a)
    
    ins = set(in_edges.keys())
    outs = set(out_edges.keys())
    
    alls = ins | outs
    
    news = outs - ins
    
    sticks = ins - outs

    for n in news:
        if len(out_edges[n]) >= 2:
            new = n
            break
    
    eights = set()
    
    alls -= sticks
    alls.remove(new)
    
    for e in alls:
        if len(out_edges[e]) == 2 and len(in_edges[e]) >= 2:
            eights.add(e)
            
    
    def bfs(graph, start):
        visited = set()
        q = deque([start])
        visited.add(start)
        
        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return visited

    cnt = 0
    
    for a in out_edges[new]:
        vis = bfs(out_edges, a)
        if not sticks & vis and not eights & vis:
            cnt += 1
        # else:
        #     cnt += 1
        #     alls = alls - vis

    answer = [new, cnt, len(sticks), len(eights)]
    return answer