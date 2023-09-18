def solution(n, m, section):
    answer = 0
    while section:
        start = section.pop(0)
        answer += 1
        while section and section[0] < start+m:
            section.pop(0)
    return answer