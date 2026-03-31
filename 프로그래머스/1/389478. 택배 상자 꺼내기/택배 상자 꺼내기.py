def solution(n, w, num):
    a, b = divmod(n, w)
    if b == 0:
        b = w
    else:
        a += 1
    c, d, = divmod(num, w)
    if d == 0:
        d = w
    else:
        c += 1
    e = a - c
    if (e%2 == 0 and b >= d) or (e%2 == 1 and (b + d) > w):
        return a - c + 1
    else:
        return a - c