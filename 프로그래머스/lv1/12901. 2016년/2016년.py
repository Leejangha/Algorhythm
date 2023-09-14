def solution(a, b):
    month = [0,3,4,0,2,5,0,3,6,1,4,6]
    day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    answer = day[(month[a-1]+b+4)%7]
    return answer