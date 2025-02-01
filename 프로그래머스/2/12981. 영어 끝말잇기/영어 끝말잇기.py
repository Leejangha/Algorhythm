def solution(n, words):
    SET = set()
    SET.add(words[0])
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in SET:
            return [i%n+1, i//n +1]
        SET.add(words[i])
    return [0,0]