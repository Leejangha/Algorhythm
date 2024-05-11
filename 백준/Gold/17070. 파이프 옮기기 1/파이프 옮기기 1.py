import sys

N = int(input())

MAP = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

ans = 0


def dfs(x, y, vector):
    global ans
    if x == N-1 and y == N-1:
        ans += 1
        return

    if vector == 0 and y < N:
        if 0 <= x < N and 0 <= y+1 < N and not MAP[x][y+1]:
            dfs(x, y+1, 0)

        if 0 <= x+1 < N and 0 <= y+1 < N and not MAP[x+1][y] and not MAP[x][y+1] and not MAP[x+1][y+1]:
            dfs(x+1, y+1, 2)

    elif vector == 1 and x < N:
        if 0 <= x+1 < N and 0 <= y < N and not MAP[x+1][y]:
            dfs(x+1, y, 1)

        if 0 <= x+1 < N and 0 <= y+1 < N and not MAP[x+1][y] and not MAP[x][y+1] and not MAP[x+1][y+1]:
            dfs(x+1, y+1, 2)

    else:
        if 0 <= x < N and 0 <= y+1 < N and not MAP[x][y+1]:
            dfs(x, y+1, 0)

        if 0 <= x+1 < N and 0 <= y < N and not MAP[x+1][y]:
            dfs(x+1, y, 1)

        if 0 <= x+1 < N and 0 <= y+1 < N and not MAP[x+1][y] and not MAP[x][y+1] and not MAP[x+1][y+1]:
            dfs(x+1, y+1, 2)


dfs(0, 1, 0)

print(ans)
