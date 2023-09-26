def solution(s):
    s = s.replace("{", "")
    s = s.replace("}", "")
    lst = list(map(int, s.split(",")))
    DICT = {}
    for num in lst:
        if num not in DICT:
            DICT[num] = 1
        else:
            DICT[num] += 1
    answer = [key for key, value in sorted(DICT.items(), key=lambda item: item[1], reverse=True)]

    return answer