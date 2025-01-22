def solution(id_list, report, k):
    # 정지시킨 유저수를 계산할 딕셔너리
    answer = {id : 0 for id in id_list}
    
    # 신고당한 유저별로 신고한 유저를 담을 딕셔너리
    DICT = {id : set() for id in id_list}
    
    # 동일한 유저에 대한 신고는 1회로 처리하므로 중복제거
    report = set(report)
    
    for rep in report:
        a, b = rep.split()
        # 나를 신고한 유저를 담음
        DICT[b].add(a)
    
    for key, value in DICT.items():
        # 신고를 k번 이상 당해 정지된 유저
        if len(value) >= k:
            # 정지된 유저를 신고한 유저의 결과 +1
            for val in value:
                answer[val] += 1
    
    # 정지시킨 결과 수를 리스트로 변환
    answer = list(answer.values())
    return answer