def solution(brown, yellow):
    answer = []
    for num in range(1,yellow+1):
        if yellow%num == 0:
            if (num+2)*2 + yellow//num*2 == brown:
                answer.append(num+2)
                answer.append(yellow//num+2)
                break
    answer.sort(reverse=True)
    return answer