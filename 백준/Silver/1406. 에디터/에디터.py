import sys

front = list(sys.stdin.readline())[:-1]
M = int(sys.stdin.readline())
operators = [sys.stdin.readline().split() for _ in range(M)]

back = []

for op in operators:
    if op[0] == "L" and front:
        w = front.pop()
        back.append(w)
    elif op[0] == "D" and back:
        w = back.pop()
        front.append(w)
    elif op[0] == "B" and front:
        front.pop()
    elif op[0] == "P":
        w = op[-1]
        front.append(w)

answer = ''.join(front + back[::-1])
print(answer)
