def solution(answers):
    answer = []
    l = len(answers)
    ans1, score1 = [1, 2, 3, 4, 5]*(l//5+1), 0
    ans2, score2 = [2, 1, 2, 3, 2, 4, 2, 5]*(l//8+1), 0
    ans3, score3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(l//10+1), 0
    for i in range(l):
        if answers[i] == ans1[i]:
            score1 += 1
        if answers[i] == ans2[i]:
            score2 += 1
        if answers[i] == ans3[i]:
            score3 += 1
    scores = [score1, score2, score3]
    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx+1)
    return answer