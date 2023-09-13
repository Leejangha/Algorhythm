def solution(food):
    answer = '0'
    for idx, n in enumerate(food[::-1]):
        answer = str(len(food)-1-idx)*(n//2) + answer + str(len(food)-1-idx)*(n//2)
    return answer