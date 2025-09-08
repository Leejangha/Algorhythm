import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    b = b%4
    if b == 0:
        b=4
    comp = str(a**b)[-1]
    if comp == "0":
        print(10)
    else:
        print(comp)