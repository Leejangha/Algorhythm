def solution(s):
    answer = ''
    lst = []
    for char in s:
        lst.append(ord(char))
    lst.sort(reverse=True)
    for l in lst:
        answer += chr(l)
    return answer