def solution(X, Y):
    answer = ""
    nums = list(range(9,-1,-1))
    for i in nums:
        num = str(i)
        lx = len(X)
        ly = len(Y)
        X = X.replace(num, "")
        Y = Y.replace(num, "")
        answer += num*min(lx-len(X), ly-len(Y))
    if not answer:
        return "-1"
    if answer.count("0") == len(answer):
        return "0"
    return answer