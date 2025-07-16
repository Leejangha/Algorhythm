import sys

input = sys.stdin.read().splitlines()

front = list(input[0])
M = int(input[1])
operators = input[2:]

back = []

for op in operators:
    if op[0] == "L" and front:
        back.append(front.pop())
    elif op[0] == "D" and back:
        front.append(back.pop())
    elif op[0] == "B" and front:
        front.pop()
    elif op[0] == "P":
        front.append(op[-1])

print(''.join(front + back[::-1]))