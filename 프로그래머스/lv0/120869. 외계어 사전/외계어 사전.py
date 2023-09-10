def solution(spell, dic):
    answer = 2

    arr = []
    for word in dic:
        for char in spell:
            if char in word:
                arr.append(word)
        if arr.count(word) == len(spell):
            answer =1

    return answer