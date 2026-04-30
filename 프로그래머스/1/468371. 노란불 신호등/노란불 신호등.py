def solution(signals):
    answer = 1
    maxi = 1
    comb = []
    for g, y, r in signals:
        comb.append((range(g+1,g+y+1), g+y+r))
        maxi *= (g+y+r)
    
    while answer <= maxi:
        flag = False
        for x, y in comb:
            if answer%y in x:
                flag = True
            else:
                flag = False
                break
        if flag:
            break
        answer += 1
    
    if answer == maxi+1:
        return -1
    return answer