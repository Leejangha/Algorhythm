def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin1 = bin(arr1[i]).zfill(n)
        bin2 = bin(arr2[i]).zfill(n)
        row = ''
        for j in range(n):
            if bin1[-1-j] == '1' or bin2[-1-j] == '1':
                row = '#' + row
            else:
                row = ' ' + row
        answer.append(row)
    return answer