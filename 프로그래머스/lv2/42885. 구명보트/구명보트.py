from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        li = limit
        li -= people.pop()
        if people:
            if li - people[0] >= 0:
                li -= people.popleft()
        answer += 1
    return answer