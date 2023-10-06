def solution(n):
    dp = [1, 2, 3]
    if n <= 3:
        return n
    for i in range(3, n):
        dp.append(dp[i-1] + dp[i-2])
    answer = dp[-1] % 1234567
    return answer