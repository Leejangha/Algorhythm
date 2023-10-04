def solution(arr):
    answer = 1
    arr.sort()
    DICT = {}
    for a in arr:
        k = 2
        cnt = 0
        sqrt = int(a**0.5)
        while k <= sqrt and a != 1:
            if a % k != 0:
                k += 1
                cnt = 0
            else:
                cnt += 1
                a //= k
                if k not in DICT:
                    DICT[k] = cnt
                else:
                    if cnt > DICT[k]:
                        DICT[k] = cnt
        if a > 1:
            if a not in DICT:
                DICT[a] = 1
    for k, v in DICT.items():
        answer *= (k**v)
    return answer