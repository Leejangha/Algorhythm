def solution(people, limit):
    answer = 0
    people.sort()
    MIN, MAX = 0, len(people) - 1
    while MIN <= MAX:
        if people[MIN] + people[MAX] <= limit:
            MIN += 1
        MAX -= 1
        answer += 1
    return answer