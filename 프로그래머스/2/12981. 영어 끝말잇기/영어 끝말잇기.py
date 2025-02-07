def solution(n, words):
    # 앞에 얘기한 단어를 중복해서 말하면 탈락이므로 집합으로 말한 단어를 저장
    SET = {words[0]}
    for i in range(1, len(words)):
        # 전 단어의 끝말과 시작이 다른 단어를 얘기하거나 이미 말한 단어를 얘기하면 탈락
        if words[i-1][-1] != words[i][0] or words[i] in SET:
            # 탈락자의 번호는 순서를 사람수로 나눈 나머지, 차례는 몫
            return [i%n+1, i//n +1]
        SET.add(words[i])
    return [0,0]