def solution(left, right):
    answer = 0
    numbers = list(range(left, right+1))
    for num in numbers:
        cnt = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                cnt += 2
        if int(num**0.5)**2 == num:
            cnt -= 1
        if cnt%2 == 0:
            answer += num
        else:
            answer -= num
    return answer