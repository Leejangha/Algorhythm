def solution(sizes):
    for i in range(len(sizes)):
        sizes[i][0], sizes[i][1] = max(sizes[i]), min(sizes[i])
    row = max(s[0] for s in sizes)
    col = max(s[1] for s in sizes)
    answer = row * col
    return answer