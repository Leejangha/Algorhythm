def solution(n):
    ans = 0
    # 현재까지 온 거리가 길어야 순강이동 했을 때 이득이므로 반대로 2로 나눠가면서 계산
    while n != 0:
        # 2로 나눠지면 나눔
        if n % 2 == 0:
            n //= 2
        # 한칸씩 움직여가며 계산
        else:
            n -= 1
            ans += 1
    return ans