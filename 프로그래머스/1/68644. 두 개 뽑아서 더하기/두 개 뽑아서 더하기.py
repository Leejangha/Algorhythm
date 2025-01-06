def solution(numbers):
    # 두 수를 더해서 만들 수 있는 수는 중복이 없어야 하므로 집합 구조를 사용
    SET = set()
    l = len(numbers)
    # i번째 인데스 수와 i+1 부터 l까지 수들의 각각 합을 집합에 추가
    for i in range(l-1):
        for j in range(i+1,l):
            SET.add(numbers[i]+numbers[j])
    # 집합을 정렬된 리스트로 변환
    answer = sorted(SET)
    return answer