def solution(cards):
    box = []
    answer = []
    j = 0
    
    for i in range(len(cards)):
        if cards[i] not in box:
            cnt = 1
            box.append(cards[i])

            while cards[box[j] - 1] not in box:
                box.append(cards[box[j] - 1])
                j += 1
                cnt += 1
                
            answer.append(cnt)
            j += 1
    if len(answer) == 1:
        return 0
    answer.sort()
    max_mul = answer[-1] * answer[-2]

    return max_mul