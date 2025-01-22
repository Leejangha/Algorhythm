def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict = {}
    for id in id_list:
        id_dict[id] = 0
    reports = set(report)
    mail = []
    for r in reports:
        user, decl = r.split()
        mail.append((user,decl))
        id_dict[decl] += 1
    for decl, cnt in id_dict.items():
        if cnt >= k:
            for m in mail:
                if m[1] == decl:
                    answer[id_list.index(m[0])] += 1
    return answer