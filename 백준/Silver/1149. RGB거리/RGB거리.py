N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    MAP[i][0] += min(MAP[i-1][1], MAP[i-1][2])
    MAP[i][1] += min(MAP[i-1][0], MAP[i-1][2])
    MAP[i][2] += min(MAP[i-1][0], MAP[i-1][1])

print(min(MAP[-1]))