def solution(phone_book):
    # 문자열을 정렬하면 첫번째 자리부터 순서대로, 길이 순서대로 정렬 되므로 바로 뒷 번호랑만 비교하면 됨
    phone_book.sort()

    for i in range(len(phone_book)-1):
        # 뒷 번호가 현재 번호로 시작하는 경우 접두어임
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True