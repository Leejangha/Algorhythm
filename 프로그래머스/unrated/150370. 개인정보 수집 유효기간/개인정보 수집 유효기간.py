def solution(today, terms, privacies):
    answer = []
    term = {}
    for t in terms:
        term[t[0]] = int(t[2:])
    user = 1
    for privacie in privacies:
        y, m, d = privacie[:-2].split('.')
        y_plus, month = divmod(int(m) + term[privacie[-1]], 12)
        if month == 0:
            month = 12
            y_plus -= 1
        year = int(y) + y_plus
        pri = str(year)+"."+str(month).rjust(2, '0')+"."+d
        print(pri, today)
        if pri <= today:
            answer.append(user)
        user += 1
    return answer
