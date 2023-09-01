def solution(n):
    if n == 1:
        return 4
    answer = -1
    start = 1
    end = n/2
    while end >= start:
        mid = (start+end)//2
        if mid**2 == n:
            answer = (mid+1)**2
            break
        elif mid**2 > n:
            end = mid-1
        else:
            start = mid+1
    return answer
