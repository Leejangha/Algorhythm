from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    # 코스 종류별로 메뉴 구성을 담을 딕셔너리
    DICT = {i: defaultdict(int) for i in course}
    
    # 코스 종류별로 메뉴 구성의 조합이 나온 횟수를 딕셔너리에 담음
    for co in course:
        for order in orders:
            if len(order) >= co:
                for com in list(map(''.join, combinations(sorted(list(order)), co))):
                    DICT[co][com] += 1

    # 각 코스별로 가장 많이 주문된 메뉴 구성들을 정답에 담음
    for _, dic in DICT.items():
        if dic.values():
            max_ = max(dic.values())
            if max_ >= 2:
                for key, value in dic.items():
                    if value == max_:
                        answer.append(key)

    # 최종 결과는 문자열순으로 정렬
    answer = sorted(answer)
    return answer