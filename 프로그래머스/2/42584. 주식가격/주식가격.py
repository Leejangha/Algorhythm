def solution(prices):
    l = len(prices)
    answer = [0]*l
    stack = []

    # 인덱스와 함께 반복
    for i, price in enumerate(prices):
        while stack and price < stack[-1][1]:
            last = stack.pop()[0]
            answer[last] = i - last
        stack.append((i, price))

    # 끝까지 가격이 떨어지지 않은 기록이 stack에 남아 있으므로 전체 시간에서 뺀만큼 기록
    for i, price in stack:
        answer[i] = l - i -1

    return answer