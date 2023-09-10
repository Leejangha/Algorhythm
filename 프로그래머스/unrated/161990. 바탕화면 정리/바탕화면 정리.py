def solution(wallpaper):
    x = []
    y = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)

    lux, luy = min(x), min(y)
    rdx, rdy = max(x)+1, max(y)+1

    return [lux, luy, rdx, rdy]