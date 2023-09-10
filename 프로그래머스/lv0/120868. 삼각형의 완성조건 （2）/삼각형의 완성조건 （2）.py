def solution(sides):
    max_len = sum(sides)
    answer = max_len - 1
    for l in range(1, max_len):
        if min(sides) + l <= max(sides):
            answer -= 1
    return answer