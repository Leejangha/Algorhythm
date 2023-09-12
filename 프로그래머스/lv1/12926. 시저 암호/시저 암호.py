def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            answer += char
        elif char.islower():
            answer += chr(ord(char)+n-26*((ord(char)+n)//123))
        else:
            answer += chr(ord(char)+n-26*((ord(char)+n)//91))
    return answer
