from itertools import permutations


def solution(n, weak, dist):
    l = len(weak)
    ld = len(dist)
    answer = ld+ 1
    weak = weak + [w + n for w in weak]
    
    for start in range(l):
        for perm in permutations(dist):
            cnt = 1
            end = weak[start] + perm[cnt - 1]

            for i in range(start, start + l):
                if weak[i] > end:
                    cnt += 1
                    if cnt > ld:
                        break
                    end = weak[i] + perm[cnt - 1]

            answer = min(answer, cnt)

    if answer >= ld + 1:
        return -1
    return answer
