def solution(s):
    answer = []
    tuples = sorted(list(s[2:-2].split("},{")), key = len)
    for idx, tup in enumerate(tuples):
        tup = list(tup.split(","))
        i = 0
        while i <= idx:
            if int(tup[i]) not in answer:
                answer.append(int(tup[i]))
            i += 1
                
    return answer