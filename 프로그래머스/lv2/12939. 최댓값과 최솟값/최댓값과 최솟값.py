def solution(s):
    numbers = sorted(list(map(int, s.split())))
    answer = str(numbers[0]) + " "+ str(numbers[-1])
    return answer