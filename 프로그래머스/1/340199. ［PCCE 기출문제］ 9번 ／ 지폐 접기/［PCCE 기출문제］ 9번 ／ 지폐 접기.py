def solution(wallet, bill):
    answer = 0
    X, Y = max(wallet), min(wallet)
    while True:
        if max(bill) <= X and min(bill) <= Y:
            break
        bill = [max(bill)//2, min(bill)]
        answer += 1
    return answer