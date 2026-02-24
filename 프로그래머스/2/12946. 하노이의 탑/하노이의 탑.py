def hanoi(n, start, through, end, ans):
    if n == 1:
        return ans.append([start, end])
    else:
        hanoi(n-1, start, end, through, ans)
        ans.append([start, end])
        hanoi(n-1, through, start, end, ans)
        return ans
        

def solution(n):
    ans = hanoi(n, 1, 2, 3, [])
    return ans

