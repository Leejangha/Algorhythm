def solution(numbers, target):
    idx = list(range(len(numbers)))
    res = []
    answer = 0
    for i in range(1<<len(idx)):
        subset = []
        for j in range(len(idx)):
            if i & (1<<j):
                subset.append(idx[j])
        res.append(subset)
    for i in res:
        num_lst = numbers[:]
        for char in i:
            num_lst[char] *= -1
        if sum(num_lst) == target:
            answer += 1
    return answer