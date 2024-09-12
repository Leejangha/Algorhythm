def solution(numbers):
    l = len(numbers)
    answer = [-1]*l
    stack = [] # 뒷 큰수를 찾지 못한 수의 인데스를 담을 스택
    
    for i in range(l):
        while stack and numbers[stack[-1]] < numbers[i]: # 뒷 큰수를 찾지 못한 수가 있으면서 현재 숫자가 그 수의 뒷 큰수일 경우
            answer[stack.pop()] = numbers[i]
        stack.append(i)
        
    return answer