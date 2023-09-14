def solution(cards1, cards2, goal):
    answer = 'Yes'
    while goal:
        if cards1:
            c1 = cards1.pop(0)
        if cards2:
            c2 = cards2.pop(0)
        g = goal.pop(0)
        if g == c1:
            cards2.insert(0, c2)
        elif g == c2:
            cards1.insert(0, c1)
        else:
            answer = 'No'
            break
    return answer