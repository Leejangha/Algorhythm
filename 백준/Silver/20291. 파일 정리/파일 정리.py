N = int(input())
files = [input().split('.') for _ in range(N)]
exts = {}
for file in files:
    ext = file[1]
    if ext not in exts:
        exts[ext] = 1
    else:
        exts[ext] += 1
answer = sorted(list(exts.keys()))
for ans in answer:
    print(f'{ans} {exts[ans]}')
