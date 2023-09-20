def solution(ingredient):
    answer = 0
    idx = 0
    while True:
        if ingredient[idx:idx+4] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                ingredient.pop(idx)
            idx -= 3
        else:
            idx += 1
        if idx > len(ingredient) - 3:
            break
    return answer