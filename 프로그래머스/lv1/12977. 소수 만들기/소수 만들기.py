def solution(nums):
    answer = 0
    num_list = combination(nums)
    for num in num_list:
        if prime_num(num) == True:
            answer += 1

    return answer

# 소수 판별
def prime_num(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


# 조합
def combination(numbers):
    combinations = []
    for i in range(len(numbers)-2):
        for j in range(i +1 , len(numbers)-1):
            for k in range(j+ 1, len(numbers)):
                sum = 0
                sum = numbers[i] + numbers[j] + numbers[k]
                combinations.append(sum)
    return combinations