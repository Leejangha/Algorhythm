# 합이 s가 되고 n개의 자연수로 이루어진 집합중 각 원소의 곱이 최대가 되는 집합을 구하는 함수
def solution(n, s):
    best_set = []
    # 남는 원소수 만큼 몫으로 채움
    best_set += [s // n for _ in range(n - s % n)]
    # 나머지를 몫에 분배
    best_set += [s // n + 1 for _ in range(s % n)]
    # 최고의 집합이 없는 경우 [-1]을 출력
    if 0 in best_set:
        return [-1]

    return best_set