def solution(players, callings):
    Dict = {}
    for rank, player in enumerate(players):
        Dict[player] = rank
    Dict2 = {v: k for k, v in Dict.items()}
    for calling in callings:
        now = Dict.get(calling)
        next = Dict2.get(now-1)
        Dict[calling] -= 1
        Dict[next] += 1
        Dict2[now] = next
        Dict2[now-1] = calling
    answer = sorted(Dict,key=lambda x:Dict[x])
    return answer