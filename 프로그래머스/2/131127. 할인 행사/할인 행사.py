from collections import Counter

def solution(want, number, discount):
    answer = 0
    arr = dict(zip(want,number))
    for i in range(len(discount)-9):
        ls = Counter(discount[i:i+10])
        if arr == ls:
            answer += 1
    return answer