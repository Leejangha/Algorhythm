def solution(N, stages):
    fail = [0]*N
    n = len(stages)

    for stage in stages:
        if stage <= N:
            fail[stage-1] += 1

    fail_rate = []
    for i in range(N):
        if n == 0:
            fail_rate.append((i+1, 0))
        else:
            fail_rate.append((i+1, fail[i]/n))
            n -= fail[i]

    fail_rate.sort(key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in fail_rate]
    return answer