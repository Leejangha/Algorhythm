front = list(input())
M = int(input())

back = []

for _ in range(M):
    op = input()
    if op == "L" and front:
        w = front.pop()
        back.append(w)
    elif op == "D" and back:
        w = back.pop()
        front.append(w)
    elif op == "B" and front:
        front.pop()
    elif op[0] == "P":
        w = op[-1]
        front.append(w)

answer = ''.join(front + back[::-1])
print(answer)