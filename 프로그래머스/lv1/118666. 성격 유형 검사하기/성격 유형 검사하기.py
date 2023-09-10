def solution(survey, choices):
    answer = ''
    mbti = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        c = choices[i]
        s = survey[i]
        if c < 4:
            mbti[s[0]] += (4-c)
        elif c > 4:
            mbti[s[1]] += (c-4)
    lst_k = list(mbti.keys())
    lst_v = list(mbti.values())
    for i in range(4):
        if lst_v[2*i] >= lst_v[2*i+1]:
            answer += lst_k[2*i]
        else:
            answer += lst_k[2*i+1]
    return answer