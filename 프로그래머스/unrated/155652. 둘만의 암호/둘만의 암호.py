def solution(s, skip, index):
    answer = ''
    alpha = list(range(ord("a"),ord("z")+1))
    skip = [ord(x) for x in skip]
    alpha = list(set(alpha) - set(skip))
    for char in s:
        idx = alpha.index(ord(char))
        answer += chr(alpha[(idx+index)%len(alpha)])
    return answer