def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    cnt_1 = bin_n.count("1")
    for num in range(n+1, 1000000):
        if bin(num).count("1") == cnt_1:
            answer = num
            break
    return answer