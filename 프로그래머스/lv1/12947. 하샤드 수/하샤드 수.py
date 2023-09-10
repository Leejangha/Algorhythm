def solution(x):
    answer = True
    y = 0
    for char in str(x):
        y += int(char)
    if x%y != 0:
        answer = False
    return answer