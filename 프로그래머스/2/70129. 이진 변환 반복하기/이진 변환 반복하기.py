def solution(s):
    zeros = 0
    i = 0
    while s != "1":
        l = len(s)
        l2 = len(s.replace("0", ""))
        zeros += (l - l2)
        s = bin(l2)[2:]
        i += 1
    return [i, zeros]