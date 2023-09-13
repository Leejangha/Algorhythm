def solution(numbers):
    SET = set()
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1,l):
            SET.add(numbers[i]+numbers[j])
    answer = sorted(SET)
    return answer