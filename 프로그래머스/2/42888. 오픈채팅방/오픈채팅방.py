from collections import defaultdict

def solution(record):
    answer = []
    nick_table = defaultdict(str)

#     for r in record:
#         if r[0] == "L":
#             act, uid = r.split()
#             answer.append((uid, act))

#         else:
#             act, uid, nick = r.split()
#             if act == "Enter":
#                 nick_table[uid] = nick
#                 answer.append((uid, act))
#             else:
#                 nick_table[uid] = nick

#     for i in range(len(answer)):
#         uid, act = answer[i]
#         if act == "Enter":
#             answer[i] = nick_table[uid] + "님이 들어왔습니다."
#         else:
#             answer[i] = nick_table[uid] + "님이 나갔습니다."
    for r in record:
        if r[0] != "L":
            act, uid, nick = r.split()
            nick_table[uid] = nick

    for r in record:
        if r[0] == "E":
            answer.append(nick_table[r.split()[1]] + "님이 들어왔습니다.")
        elif r[0] == "L":
            answer.append(nick_table[r.split()[1]] + "님이 나갔습니다.")

    return answer