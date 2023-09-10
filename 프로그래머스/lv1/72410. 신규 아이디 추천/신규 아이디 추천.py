def solution(new_id):
    new1 = new_id.lower()   # 대문자를 소문자로 변경
    new2 = ''
    for char in new1:
        if not char.isalpha() and not char.isdecimal() and char not in ['-', '_', '.']:
            continue    # 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
        else:
            new2 += char
    new3 = new2[0]
    for i in range(1, len(new2)):
        if new2[i] == '.' and new3[-1] == '.':
            continue    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
        new3 += new2[i]
    new4 = new3.strip(".")  # 마침표(.)가 처음이나 끝에 위치한다면 제거
    if not new4:
        new4 = "a"  # 빈 문자열이라면, "a"를 대입
    if len(new4) >= 16:
        new4 = new4[:15]    # 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    new6 = new4.strip(".")  # 마침표(.)가 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    while len(new6) < 3:
        new6 += new6[-1]    # 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    answer = new6
    return answer