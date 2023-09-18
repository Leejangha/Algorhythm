def solution(n):
    numbers = [False, False] + ([True] * (n-1))
    for i in range(2, int(n**0.5)+1):
        if numbers[i]:
            j = 2
            while i*j < n+1:
                numbers[i*j] = False
                j += 1
    answer = numbers.count(True)
    return answer