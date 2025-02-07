def solution(nums):
    # 전체 포켓몬의 종류가 N/2보다 작을 경우에는 종류의 수만큼 만 고를 수 있음
    return min(len(nums)//2, len(set(nums)))