def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for c in can:
            if c in bab and c*2 not in bab:
                bab = bab.replace(c, " ")
        bab = bab.strip(" ")
        if not bab:
            answer += 1
    return answer