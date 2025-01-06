def solution(arr1, arr2):
    # arr1의 열과 arr2의 행을 차례대로 곱해야함
    # arr1의 열을 먼저 반복
    # arr2의 행을 반복하기 위해 언패킹(*)후 패킹(zip)하여 행렬 변환함
    # 열과 행의 값을 인덱스 순대로 곱해서 합해야 하므로 패킹(zip)하여 반복
    return [[sum([a*b for a, b in zip(row, col)]) for col in zip(*arr2)] for row in arr1]