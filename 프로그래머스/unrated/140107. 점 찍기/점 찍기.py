def solution(k, d):
    count = 0
    i = 0
    x_list = []
    while i * k <= d:
        x_list.append(i * k)
        i += 1
    for x in x_list:
        y_limit = int((d**2-x**2)**0.5/k)
        count += y_limit + 1
    return count
solution(2,4)