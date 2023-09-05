def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6 or not s.isdigit():
        answer = False
    return answer