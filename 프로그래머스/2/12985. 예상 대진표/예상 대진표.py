def solution(n,a,b):
    for i in range(1, n//2 + 1):
        # 해당 라운드에서 몇번째 게임을 하는지 계산
        a = (a+1)//2
        b = (b+1)//2
        
        # 같은 게임을 하는경우 서로가 맞붙음
        if a == b:
            return i

    return