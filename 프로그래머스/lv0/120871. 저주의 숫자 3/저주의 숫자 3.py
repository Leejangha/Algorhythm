def solution(n):
    lst = []
    num = 1
    while len(lst) < n:
        if num % 3 != 0 and '3' not in str(num):
            lst.append(num)
        num += 1
    answer = lst[-1]
    return answer