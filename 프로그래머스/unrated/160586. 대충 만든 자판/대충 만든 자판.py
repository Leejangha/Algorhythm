def solution(keymap, targets):
    answer = []
    DICT = {}
    for key in keymap:
        for idx, k in enumerate(key):
            if k not in DICT:
                DICT[k] = idx+1
            else:
                if idx+1 < DICT[k]:
                    DICT[k] = idx+1
    for target in targets:
        cnt = 0
        for t in target:
            if t not in DICT:
                cnt = -1
                break
            else:
                cnt += DICT[t]
        answer.append(cnt)
    return answer