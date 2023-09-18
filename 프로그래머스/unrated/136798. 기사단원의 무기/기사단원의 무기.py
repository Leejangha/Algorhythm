def solution(number, limit, power):
    divisors = [1]
    for num in range(2, number+1):
        divisor = 1
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                divisor += 1
        if num**0.5 == int(num**0.5):
            if divisor*2-1 <= limit:
                divisors.append(divisor*2-1)
            else:
                divisors.append(power)
        else:
            if divisor*2 <= limit:
                divisors.append(divisor*2)
            else:
                divisors.append(power)
    answer = sum(divisors)
    return answer