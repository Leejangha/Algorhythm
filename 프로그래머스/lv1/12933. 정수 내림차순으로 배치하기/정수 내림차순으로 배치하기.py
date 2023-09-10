def solution(n):
    lst = []
    for num in str(n):
        lst.append(num)
    lst.sort(reverse=True)
    answer = int(''.join(lst))
    return answer