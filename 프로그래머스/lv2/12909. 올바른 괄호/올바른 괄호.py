def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
            else:
                return False
    if stack:
        return False
    return True