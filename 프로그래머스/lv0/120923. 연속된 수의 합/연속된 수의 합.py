def solution(num, total):
    answer = []
    x = total//num
    for i in range(num):
        answer.append(x+num//2-i)
    answer.sort()
    return answer