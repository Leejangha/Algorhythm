def solution(n, k):
    answer = 0
    num = ""
    i = 1
    while n > 0:
        num = str(n%(k**i)) + num
        n //= (k**i)
    numbers = list(map(int, [x for x in num.split('0') if x]))
    for number in numbers:
        if number == 1:
            continue
        is_Prime = True
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                is_Prime = False
                break
        if is_Prime:
            answer += 1
    return answer