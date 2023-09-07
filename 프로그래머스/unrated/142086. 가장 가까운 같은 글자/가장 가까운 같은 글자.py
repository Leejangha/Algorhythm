def solution(s):
    answer = []
    DICT = {}
    for idx in range(len(s)):
        char = s[idx]
        if char not in DICT:
            answer.append(-1)
            DICT[char] = idx
        else:
            answer.append(idx-DICT[char])
            DICT[char] = idx
    return answer