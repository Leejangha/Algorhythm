def solution(N, stages):
    fails = [0]*(N+1)
    n = len(stages)

    # 스테이지별로 멈춰있는 유저 수 계산
    for stage in stages:
        if stage <= N:
            fails[stage] += 1

    fail_rate = []
    for i in range(1, N+1):
        # i번째 스테이지에 멈춰있는 유저 수
        fail = fails[i]

        # 스테이지에 도달한 유저가 없는 경우 실패율은 0
        # 실패율이 같은 스테이지 있을 경우 정렬해야 하므로 스테이지 번호도 튜플로 저장
        if n == 0:
            fail_rate.append((i, 0))
        else:
            # 실패율은 현재 스테이지에 멈춰있는 유저 수 / 도달한 유저 수
            fail_rate.append((i, fail/n))
            # 다음 스테이지에 도달한 유저수는 현재 스테이지에 멈춰있는 유저 수를 빼줌
            n -= fail

    # 실패율이 높은 순, 같을 경우 스테이지가 낮은 순으로 정렬
    fail_rate.sort(key=lambda x: (-x[1], x[0]))

    # 최종 출력은 스테이지 번호
    answer = [x[0] for x in fail_rate]
    return answer