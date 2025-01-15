from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # 원하는 제품과 개수를 키 : 밸류 형식의 딕셔너리로 생성
    arr = dict(zip(want,number))

    # i날짜 부터 10일 간
    for i in range(len(discount)-9):
        # 10일 간 할인하는 제품과 개수를 카운트한 딕셔너리와 arr을 비교
        ls = Counter(discount[i:i+10])
        if arr == ls:
            answer += 1
    return answer