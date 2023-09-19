def solution(s):
    answer = 0
    i = 0
    l = len(s)
    while i < l:
        x = s[i]
        cnt = 1
        for j in range(i+1, l):
            if s[j] == x:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                answer += 1
                i = j+1
                break
            if j == l-1:
                answer += 1
                return answer
        if i == l-1:
            answer += 1
            break
    return answer