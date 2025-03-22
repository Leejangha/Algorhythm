from collections import Counter

def solution(topping):
    answer = 0
    DICT = Counter(topping)
    SET = set()
    
    for top in topping:
        DICT[top] -= 1
        if DICT[top] == 0:
            del DICT[top]
        SET.add(top)
        
        if len(DICT) == len(SET):
            answer += 1
        elif len(DICT) < len(SET):
            break
    
    return answer