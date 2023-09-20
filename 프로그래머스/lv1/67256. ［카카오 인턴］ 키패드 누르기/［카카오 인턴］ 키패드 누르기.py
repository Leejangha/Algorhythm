delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(numbers, hand):
    answer = ''
    # keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    now_left = (3, 0)
    now_right = (3, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            now_left = (number//3, 0)
            answer += "L"
        elif number in [3, 6, 9]:
            now_right = (number//3-1, 2)
            answer += "R"
        else:
            if number == 0:
                now = (3, 1)
            else:
                now = (number//3, 1)
            dis_left = abs(now[0]-now_left[0]) + abs(now[1]-now_left[1])
            dis_right = abs(now[0]-now_right[0]) + abs(now[1]-now_right[1])
            print(now, now_left, now_right)
            if dis_right < dis_left:
                now_right = now
                answer += "R"
            elif dis_left < dis_right:
                now_left = now
                answer += "L"
            else:
                if hand == "right":
                    now_right = now
                    answer += "R"
                else:
                    now_left = now
                    answer += "L"
    return answer
