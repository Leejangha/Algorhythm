def solution(nums):
    N = len(nums)
    kinds = {}
    for num in nums:
        kinds[num] = 1
    if len(list(kinds.keys())) < N/2:
        answer = len(list(kinds.keys()))
    else :
        answer = N/2
    return answer