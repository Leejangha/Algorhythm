def solution(genres, plays):
    answer = []
    DICT = {}
    sum_plays = {}
    
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        if g not in DICT:
            DICT[g] = [(i,p)]
            sum_plays[g] = p
        else:
            sum_plays[g] += p
            DICT[g].append((i,p))

    sum_plays = sorted(sum_plays.items(), key=lambda x : x[1], reverse=True)
    
    for genre, _ in sum_plays:
        songs = sorted(DICT[genre], key=lambda x : x[1], reverse=True)
        
        if len(songs) == 1:
            answer.append(songs[0][0])
        else:
            for i in range(2):
                answer.append(songs[i][0])
    
    return answer