def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    # 원하는 단어 배열을 하나씩 순서대로 탐색
    for g in goal:
        # 두 카드 뭉치에는 서로 다른 단어들만 존재하므로 조건문으로 둘중 하나의 첫번째 카드와 같을 경우 카드 뭉치에서 제거
        if cards1 and g == cards1[0]:
            cards1.pop(0)
        elif cards2 and g == cards2[0]:
            cards2.pop(0)
        # 카드 뭉치에서 순서대로 카드를 꺼내야 하므로 두 뭉치의 첫번째 카드 중 원하는 단어가 없는 경우 완성하지 못함
        else:
            answer = 'No'
    return answer