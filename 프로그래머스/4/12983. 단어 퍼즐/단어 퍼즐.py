def solution(strs, t):
    DP = [float('inf')] * len(t)
    strs = set(strs)
    
    for i in range(len(t)):
        for j in range(min(5, i+1),-1,-1):
            if t[i-j:i+1] in strs:
                if i == j:
                    DP[i] = 1
                else:
                    DP[i] = min(DP[i], DP[i-j-1]+1)

    if DP[-1] == float('inf'):
        return -1 
    else:
        return DP[-1]
