def solution(s):
    cnt = 0
    cnt_zero = 0
    while s != "1":
        before = len(s)
        zero = s.count("0")
        cnt += 1
        cnt_zero += zero
        s = bin(before-zero)[2:]
    answer = [cnt, cnt_zero]
    return answer