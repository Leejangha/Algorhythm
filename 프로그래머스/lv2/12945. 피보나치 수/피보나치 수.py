def solution(n):
    F = [0, 1]
    def fibo(n):
        for i in range(2, n+1):
            F.append(F[i-1] + F[i-2])
        return F[n]
    answer = fibo(n)%1234567
    return answer