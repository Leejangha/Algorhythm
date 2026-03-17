def if_op(op_start, op_end, pos):
    if op_start <= pos <= op_end:
        return op_end
    else:
        return pos

def formating(pos, command):
    times = int(pos[:2])*60 + int(pos[-2:])
    if command == "next":
        times += 10
    else:
        times -= 10
    mm, ss = divmod(times, 60)
    if mm < 0:
        return "00:00"
    else:
        if mm < 10:
            mm = "0" + str(mm)
        if ss < 10:
            ss = "0" + str(ss)
        return str(mm) + ":" + str(ss)
    
def solution(video_len, pos, op_start, op_end, commands):
    for command in commands:
        pos = if_op(op_start, op_end, pos)
        pos = min(formating(pos, command), video_len)
        pos = if_op(op_start, op_end, pos)
    return pos