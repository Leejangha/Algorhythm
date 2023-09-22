def solution(s):
    answer = []
    lst = s.split(" ")
    for char in lst:
        if char:
            answer.append(char.capitalize())
        else:
            answer.append("")
    answer = " ".join(answer)
    return answer