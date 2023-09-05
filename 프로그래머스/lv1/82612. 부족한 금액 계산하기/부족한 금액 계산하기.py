def solution(price, money, count):
    for cnt in range(1,count+1):
        money -= price*cnt
    if money > 0:
        return 0
    answer = money*-1
    return answer