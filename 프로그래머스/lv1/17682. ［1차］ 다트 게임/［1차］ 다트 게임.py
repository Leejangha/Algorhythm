bonus = {'S': 1, 'D': 2, 'T': 3}

def solution(dartResult):
    arr = list(dartResult)
    i = 0
    while i < len(dartResult)-1:
        if arr[i:i+2] == ['1', '0']:
            arr[i] = '10'
            arr.pop(i+1)
        i += 1
    lst = []
    for char in arr:
        if char.isdigit():
            lst.append(int(char))
        elif char.isalpha():
            num = lst.pop()
            lst.append(num**bonus[char])
        else:
            if char == '*':
                lst[-1] *= 2
                if len(lst) > 1:
                    lst[-2] *= 2
            else:
                lst[-1] *= -1
    answer = sum(lst)
    return answer