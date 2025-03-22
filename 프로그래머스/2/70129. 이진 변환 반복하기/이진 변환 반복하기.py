def solution(s):
    zeros, i = 0, 0
    while s != "1":
        l = s.count("1")
        zeros += (len(s) - l)
        s = bin(l)[2:]
        i += 1
    return [i, zeros]