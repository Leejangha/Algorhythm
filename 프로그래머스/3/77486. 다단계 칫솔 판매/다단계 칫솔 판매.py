def solution(enroll, referral, seller, amount):
    # 판매원별 수익금을 저장할 딕셔너리
    answer = {en : 0 for en in enroll}
    
    # 판매원과 추천인을 연결
    DICT = dict(zip(enroll, referral))
    
    for sell, amt in zip(seller, amount):
        amt *= 100
        tips = amt//10
        # 판매자에 수수료를 제외한 수익을 더함
        answer[sell] += (amt-tips)
        refer = DICT[sell]
        # 추천인의 수익은 판매자의 수수료
        amt = tips

        # 추천인이 센터거나 수수료가 0원일때까지 반복
        while refer != "-" and tips != 0:
            tips //= 10
            answer[refer] += (amt-tips)

            refer = DICT[refer]

            # 그냥 한줄 덜 실행하려고 넣음
            if refer == "-":
                break

            amt = tips

    answer = list(answer.values())
    
    return answer