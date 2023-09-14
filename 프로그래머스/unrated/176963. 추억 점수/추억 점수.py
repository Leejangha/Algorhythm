def solution(name, yearning, photo):
    answer = []
    for pho in photo:
        point = 0
        for i in range(len(name)):
            point += yearning[i]*pho.count(name[i])
        answer.append(point)
    return answer