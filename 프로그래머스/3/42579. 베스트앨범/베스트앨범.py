def solution(genres, plays):
    answer = []
    
    # 장르별로 노래를 담아 재생수로 정렬할 딕셔너리
    DICT = {}
    # 장르별 재생 횟수를 담을 딕셔너리
    sum_plays = {}
    
    # 기준 3번에 고유번호를 봐야하므로 인덱스도 같이 반복
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in DICT:
            DICT[g] = [(i,p)]
            sum_plays[g] = p
        else:
            sum_plays[g] += p
            DICT[g].append((i,p))

    # 재생된 횟수를 기준으로 내림차순 정렬
    sum_plays = sorted(sum_plays.items(), key=lambda x : x[1], reverse=True)
    
    # 많이 재생된 장르의 노래부터 탐색
    for genre, _ in sum_plays:
        # 같은 장르 내에서 재생된 횟수를 기준으로 내림차순 정렬(처음 리스트에 넣을때 인덱스 순으로 넣었으므로 횟수가 같을 경우 낮은 인덱스가 먼저임)
        songs = sorted(DICT[genre], key=lambda x : x[1], reverse=True)[:2]
        
        for song, _ in songs:
            answer.append(song)
    
    return answer