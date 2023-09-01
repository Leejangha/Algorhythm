def solution(n):
    answer = []
    for char in str(n)[::-1]:
        answer.append(int(char))
    return answer