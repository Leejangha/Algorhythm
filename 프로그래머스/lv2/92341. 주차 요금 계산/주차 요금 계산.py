import math
from _datetime import datetime


def convert_second_to_hour_minute_second(second):
    hour = second // 3600
    minute = (second // 60) - (hour * 60)
    sec = second - (minute * 60) - (hour * 3600)

    return hour, minute, sec


def solution(fees, records):
    answer = []
    ft, ff, dt, df = fees
    DICT = {}
    fee = {}
    lst = []
    for record in records:
        t, num, status = record.split(" ")
        t = datetime.strptime(t, "%H:%M")
        if status == "IN":
            DICT[num] = t
        else:
            if num not in fee:
                fee[num] = t - DICT[num]
            else:
                fee[num] += t - DICT[num]
            DICT.pop(num)
    if DICT:
        for k, v in DICT.items():
            if k not in fee:
                fee[k] = datetime.strptime('23:59', "%H:%M") - v
            else:
                fee[k] += datetime.strptime('23:59', "%H:%M") - v
    for k, v in fee.items():
        lst.append((k, v.total_seconds() / 60))
    lst.sort()
    for l in lst:
        answer.append(int(ff + math.ceil((max(l[1] - ft, 0)/dt))*df))
    return answer