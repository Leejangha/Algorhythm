from collections import defaultdict
import operator

def solution(k, tangerine):
    answer = 0
    DICT = defaultdict(int)
    for tang in tangerine:
        DICT[tang] += 1
    lst = sorted(DICT.items(), key=operator.itemgetter(1), reverse=True)
    for a, b in lst:
        k -= b
        answer += 1
        if k <= 0:
            break
    return answer