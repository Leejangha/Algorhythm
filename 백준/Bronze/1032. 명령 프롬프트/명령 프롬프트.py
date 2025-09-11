import sys

N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    lst.append(list(sys.stdin.readline()[:-1]))

answer = ''

for l in zip(*lst):
    s = set(l)
    if len(s) == 1:
        answer += list(s)[0]
    else:
        answer += '?'

print(answer)