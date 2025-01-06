def solution(answers):
    # 수포자별로 찍는 패턴에 맞는 답안을 리스트로 만듬
    l = len(answers)
    ans1 = [1, 2, 3, 4, 5]*(l//5+1)
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]*(l//8+1)
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(l//10+1)

    # 삼인방의 점수 배열
    scores = [0, 0, 0]

    # 문제의 번호와 답을 동시에 반복해야 하므로 enumerate 내장 함수를 사용
    for i, ans in enumerate(answers):
        if ans1[i] == ans:
            scores[0] += 1
        if ans2[i] == ans:
            scores[1] += 1
        if ans3[i] == ans:
            scores[2] += 1

    # 최고 점수
    max_score = max(scores)

    # 최고 점수가 여러명일 경우 오름차순이므로 1번부터 순차적으로 탐색
    answer = []
    for i, score in enumerate(scores):
        if score == max_score:
            # i는 0부터 시작하므로 +1
            answer.append(i+1)
    return answer