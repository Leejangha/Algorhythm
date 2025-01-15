from collections import defaultdict

def solution(record):
    answer = []
    nick_table = defaultdict(str)

    # 방에 입장하거나 닉을 변경하는 경우 닉네임 테이블에 저장
    for r in record:
        if r[0] != "L":
            act, uid, nick = r.split()
            nick_table[uid] = nick

    # 방에 입장하거나 나가는경우 닉네임 테이블에 저장된 최종 닉네임을 출력
    for r in record:
        if r[0] == "E":
            answer.append(nick_table[r.split()[1]] + "님이 들어왔습니다.")
        elif r[0] == "L":
            answer.append(nick_table[r.split()[1]] + "님이 나갔습니다.")

    return answer