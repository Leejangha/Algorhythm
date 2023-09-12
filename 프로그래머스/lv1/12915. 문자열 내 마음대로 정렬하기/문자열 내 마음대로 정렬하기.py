def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda s: s[n])
    return answer