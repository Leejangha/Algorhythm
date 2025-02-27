from itertools import product

def solution(n, info):
    answer = [-1]
    max_point = 0
    info.reverse()
    
    for case in product((True,False), repeat=11):
        arrows = sum(info[i]+1 for i in range(11) if case[i])
        if arrows <= n:
            l_point = sum(i for i in range(11) if case[i])
            a_point = sum(i for i in range(11) if not case[i] and info[i])
            
            if l_point - a_point > max_point:
                max_point = l_point - a_point
                answer = list(info[i]+1 if case[i] else 0 for i in range(11))
                answer[0] += n - arrows

    answer.reverse()
    return answer