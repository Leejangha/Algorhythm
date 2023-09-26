def solution(operations):
    q = []
    for oper in operations:
        if oper[0] == "I":
            q.append(int(oper[2:]))
        elif q:
            if oper == "D 1":
                q.remove(max(q))
            elif oper == "D -1":
                q.remove(min(q))
    if not q:
        answer = [0,0]
    else:
        answer = [max(q), min(q)]
    return answer