HEX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def solution(n, t, m, p):
    answer = ''
    numbers = "01"
    for i in range(2, t*m):
        number = ""
        while i != 0:
            a, b = divmod(i, n)
            if b in HEX:
                b = HEX[b]
            number = str(b) + number
            i //= n
        numbers += number
    for j in range(p-1, t*m, m):
        answer += numbers[j]
    return answer