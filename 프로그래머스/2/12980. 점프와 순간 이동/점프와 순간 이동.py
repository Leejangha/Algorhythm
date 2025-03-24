def solution(n):
    ans = 0
    # 현재까지 온 거리가 길어야 순간이동 했을 때 이득이므로 반대로 계산
    while n > 0:
        # 2로 나눠지는 만큼 나누고 안되면 1씩 움직임
        ans += n % 2
        n //= 2
    return ans