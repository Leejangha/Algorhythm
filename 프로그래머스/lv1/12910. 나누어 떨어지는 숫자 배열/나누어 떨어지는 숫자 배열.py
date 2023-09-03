def solution(arr, divisor):
    answer = []
    arr.sort()
    for ele in arr:
        if ele % divisor == 0:
            answer.append(ele)
    if not answer:
        answer.append(-1)
    return answer