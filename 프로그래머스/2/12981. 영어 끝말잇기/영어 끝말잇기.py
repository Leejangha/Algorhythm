def solution(n, words):
    SET = {words[0]}
    turn = 1
    tail = words[0][-1]
    for word in words[1:]:
        turn += 1
        head = word[0]
        if word in SET or head != tail:
            return [turn % n if turn % n != 0 else n, (turn-1) // n + 1]
        else:
            SET.add(word)
        tail = word[-1]
    return [0, 0]